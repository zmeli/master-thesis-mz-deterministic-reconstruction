import os
from core.batch_processor import analyze_and_report
from manual_testing.documenter import PermutationDocumenter

def run_permutation_tests():
    """Run the synthetic operator-permutation test suite and write its report."""
    print("\n" + "="*60)
    print("### SYNTHETIC PERMUTATION TEST (3 Operators, 4 Leaves) ###")
    print("="*60)
    
    # Define clean output paths based on the new folder structure
    report_path = "output/audit_reports/permutation_report_level_2.md"
    image_dir = "output/audit_reports/images_L2"
    
    # Initialize the test suite
    documenter = PermutationDocumenter()
    
    # levels=2 automatically generates trees with 3 operators and 4 leaves.
    # 4 possible operators ^ 3 nodes = exactly 64 permutations.
    documenter.generate_markdown_report(
        levels=2, 
        filepath=report_path, 
        image_dir=image_dir, 
        root_n=100,      # The baseline frequency to distribute
        max_sample=64    # Cap it at 64 to ensure we process the exact full set
    )

def baselineTest():
    """Run the batch processor over the stress-test folder of synthetic logs."""
    print("\n" + "="*60)
    print("### BATCH PROCESSOR ENGINE ###")
    print("="*60)

    # ==========================================
    # CONFIGURATION: Edit these variables as needed
    # ==========================================
    TARGET_DATA_PATH = "data/stress_tests/"     # Folder containing your CSV/XES files
    REPORT_OUTPUT_DIR = "output/xesTest/"                 # Where the Markdown files will be saved
    IMAGE_OUTPUT_DIR = "output/batch_images/xesTest"    # Where the Graphviz PNGs will be saved
    
    NOISE_THRESHOLD = 0             # PM4Py noise filtering (0.0 to 1.0)
    SHOW_FRAGMENTS = True             # Show subsumed sub-paths?
    SHOW_AS = True                    # Show [AS] Activity Sets?
    # ==========================================

    if not os.path.exists(TARGET_DATA_PATH):
        print(f"[-] Error: Data directory '{TARGET_DATA_PATH}' not found.")
        print("    Please create it and place your event logs inside.")
        return

    print(f"[+] Target Source : {TARGET_DATA_PATH}")
    print(f"[+] Report Output : {REPORT_OUTPUT_DIR}/")
    print(f"[+] Image Output  : {IMAGE_OUTPUT_DIR}/\n")

    # Run the batch processor
    analyze_and_report(
        target_path=TARGET_DATA_PATH,
        report_dir=REPORT_OUTPUT_DIR,
        image_dir=IMAGE_OUTPUT_DIR,
        show_fragments=SHOW_FRAGMENTS,
        show_as=SHOW_AS,
        noise_threshold=NOISE_THRESHOLD
    )


def main():
    """Run the batch processor over a single configured BPIC event-log file."""
    print("\n" + "="*60)
    print("### BATCH PROCESSOR ENGINE ###")
    print("="*60)

    # ==========================================
    # CONFIGURATION: Edit these variables as needed
    # ==========================================
    TARGET_DATA_PATH = "data/BPIC2021/Training Logs/pdc2021_0000000.xes"     # Single CSV/XES log file (a folder is also accepted)
    REPORT_OUTPUT_DIR = "output/xesTest/"                 # Where the Markdown files will be saved
    IMAGE_OUTPUT_DIR = "output/batch_images/xesTest"    # Where the Graphviz PNGs will be saved
    
    NOISE_THRESHOLD = 0             # PM4Py noise filtering (0.0 to 1.0)
    SHOW_FRAGMENTS = True             # Show subsumed sub-paths?
    SHOW_AS = True                    # Show [AS] Activity Sets?
    # ==========================================

    if not os.path.exists(TARGET_DATA_PATH):
        print(f"[-] Error: Data directory '{TARGET_DATA_PATH}' not found.")
        print("    Please create it and place your event logs inside.")
        return

    print(f"[+] Target Source : {TARGET_DATA_PATH}")
    print(f"[+] Report Output : {REPORT_OUTPUT_DIR}/")
    print(f"[+] Image Output  : {IMAGE_OUTPUT_DIR}/\n")

    # Run the batch processor
    analyze_and_report(
        target_path=TARGET_DATA_PATH,
        report_dir=REPORT_OUTPUT_DIR,
        image_dir=IMAGE_OUTPUT_DIR,
        show_fragments=SHOW_FRAGMENTS,
        show_as=SHOW_AS,
        noise_threshold=NOISE_THRESHOLD
    )

if __name__ == "__main__":
    #main()
    #run_permutation_tests()
    baselineTest()


    
