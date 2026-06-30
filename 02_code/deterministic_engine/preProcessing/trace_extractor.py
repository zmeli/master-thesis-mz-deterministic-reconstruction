import xml.etree.ElementTree as ET
from pathlib import Path
import gzip # <--- NEW IMPORT

def extract_traces_to_md(xml_file, output_md):
    """
    Parses an XES/XML process log and exports the traces into a Markdown file.
    """
    print(f"Parsing XML file: {xml_file}...")
    
    try:
        path_obj = Path(xml_file)
        # --- NEW LOGIC: Check if it is compressed ---
        if path_obj.suffix.lower() == '.gz':
            # Open as a decompressed text stream
            with gzip.open(xml_file, 'rt', encoding='utf-8') as f:
                tree = ET.parse(f)
        else:
            # Open normally
            tree = ET.parse(xml_file)
            
        root = tree.getroot()
        # ------------------------------------------
        
    except Exception as e:
        print(f"Error reading the XML file: {e}")
        return

    # Ensure the output directory exists
    Path(output_md).parent.mkdir(parents=True, exist_ok=True)

    # Open the Markdown file for writing
    with open(output_md, 'w', encoding='utf-8') as md:
        md.write(f"# Process Traces: `{Path(xml_file).name}`\n\n")
        
        # Find all traces, bypassing XML namespace restrictions with the {*} wildcard
        traces = root.findall('.//{*}trace')
        
        for i, trace in enumerate(traces, start=1):
            events = []
            
            # Find all events within this trace
            for event in trace.findall('.//{*}event'):
                # Extract the activity name from the <string key="concept:name" value="..."> tag
                concept_name = event.find('.//{*}string[@key="concept:name"]')
                if concept_name is not None:
                    events.append(concept_name.get('value'))
            
            # If the trace has events, format and write them to the MD file
            if events:
                md.write(f"### Trace {i}\n")
                md.write(" -> ".join(events) + "\n\n")
                
    print(f"Success! {len(traces)} traces have been exported to: {output_md}")

# --- Execution ---
if __name__ == "__main__":
    input_xml = 'data/BPIC2012_1_all/BPI_Challenge_2012.xes.gz'
    output_markdown = 'output/BPIC2012_gz/audit_BPI_Challenge_2012.md'
    
    extract_traces_to_md(input_xml, output_markdown)