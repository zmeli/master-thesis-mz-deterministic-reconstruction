import gzip
import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path

def get_letter_from_index(index):
    """
    Converts a number into a letter (0->A, 1->B ... 25->Z, 26->AA, 27->AB).
    Ensures we never run out of letters even if there are hundreds of unique events.
    """
    result = ""
    while index >= 0:
        result = chr(index % 26 + 65) + result
        index = index // 26 - 1
    return result

def convert_xes_to_mapped_csv(xml_file, output_csv, output_legend):
    print(f"[*] Parsing compressed XML: {xml_file}...")
    
    try:
        path_obj = Path(xml_file)
        if path_obj.suffix.lower() == '.gz':
            with gzip.open(xml_file, 'rt', encoding='utf-8') as f:
                tree = ET.parse(f)
        else:
            tree = ET.parse(xml_file)
            
        root = tree.getroot()
    except Exception as e:
        print(f"[!] Error reading the XML file: {e}")
        return

    # Data structures for processing
    data = []
    activity_map = {}
    current_char_index = 0
    
    traces = root.findall('.//{*}trace')
    print(f"[*] Found {len(traces)} cases. Extracting events...")

    for trace in traces:
        # Extract Case ID
        case_id_tag = trace.find('.//{*}string[@key="concept:name"]')
        case_id = case_id_tag.get('value') if case_id_tag is not None else "Unknown"
        
        # Process Events
        for event in trace.findall('.//{*}event'):
            # Extract Original Activity Name
            concept_tag = event.find('.//{*}string[@key="concept:name"]')
            original_activity = concept_tag.get('value') if concept_tag is not None else "Unknown"
            
            # Extract Timestamp
            time_tag = event.find('.//{*}date[@key="time:timestamp"]')
            timestamp = time_tag.get('value') if time_tag is not None else None
            
            # Map Activity to Letter
            if original_activity not in activity_map:
                activity_map[original_activity] = get_letter_from_index(current_char_index)
                current_char_index += 1
                
            mapped_activity = activity_map[original_activity]
            
            # Append to data
            data.append({
                'Case ID': case_id,
                'Activity': mapped_activity,
                'Timestamp': timestamp
            })

    # Ensure output directory exists
    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)

    # 1. Save the CSV
    print(f"[*] Building DataFrame and saving CSV...")
    df = pd.DataFrame(data)
    # Sort by Case ID and Timestamp to ensure perfect process ordering
    if 'Timestamp' in df.columns and df['Timestamp'].notnull().any():
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], utc=True)
        df = df.sort_values(by=['Case ID', 'Timestamp'])
        
    df.to_csv(output_csv, index=False, sep=',')
    print(f"    -> 💾 Saved clean CSV to: {output_csv} ({len(df)} events)")

    # 2. Save the Mapping Legend
    with open(output_legend, 'w', encoding='utf-8') as legend_file:
        legend_file.write("--- Activity Mapping Legend ---\n")
        for orig, letter in activity_map.items():
            legend_file.write(f"{letter} = {orig}\n")
    print(f"    -> 📝 Saved Legend to: {output_legend}")


if __name__ == "__main__":
    # ==========================================
    # CONFIGURATION
    # ==========================================
    
    INPUT_GZ_FILE = "data/BPIC2021/Training Logs/pdc2021_0000000.xes" 
    
    # Where to save the generated files
    OUTPUT_CSV = "data/csv/csv/xes.csv"
    OUTPUT_LEGEND = "data/csv/csv/xes"
    
    # ==========================================
    
    convert_xes_to_mapped_csv(INPUT_GZ_FILE, OUTPUT_CSV, OUTPUT_LEGEND)