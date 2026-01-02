from gooey import Gooey, GooeyParser
import datetime

@Gooey(program_name="Gooey Ultimate Enterprise CRM", default_size=(1100, 800), navigation="Tabbed")
def main():
    parser = GooeyParser(description="Comprehensive Data Intake & Account Lifecycle System")
    
    # Grouped fields for a "Form" look
    profile = parser.add_argument_group("Organization Profile")
    # 1. Text Input
    profile.add_argument("company", help="Full legal name of the entity")
    # 2. Multi-line Text
    profile.add_argument("notes", widget="Textarea", help="Internal relationship discovery notes")
    # 3. Choices (Dropdown)
    profile.add_argument("tier", choices=["Enterprise", "SME", "Education", "NGO"], help="Account market tier")
    
    config = parser.add_argument_group("System Configuration")
    # 4. Radio (Mocked by Gooey automatically for small choice sets or mutually exclusive groups)
    # 5. Checkbox (Boolean args)
    config.add_argument("-a", "--active", action="store_true", help="Set account status to ACTIVE immediately")
    config.add_argument("-m", "--marketing", action="store_true", help="Subscribe to global marketing tracks")
    
    # 7. Slider
    config.add_argument("-p", "--priority", type=int, help="Internal Priority Score (1-100)", widget="Slider")
    
    # 8. Number Input (Spinbox implicit)
    config.add_argument("-s", "--seats", type=int, help="Projected Licensed Seat Count", default=10)
    
    # 9. Date Chooser
    config.add_argument("-d", "--date", widget="DateChooser", help="Target contract signing date", default=str(datetime.date.today()))
    
    # 11. File Chooser
    config.add_argument("-c", "--contract", widget="FileChooser", help="Upload scanned Master Services Agreement (PDF)")

    # 12. Directory Chooser
    config.add_argument("-o", "--output", widget="DirChooser", help="Select directory for local data dump")

    args = parser.parse_args()
    
    print("-" * 50)
    print("CRM PROCESSING CONSOLE")
    print("-" * 50)
    print(f"COMMITTING RECORD: {args.company}")
    print(f"TIER:              {args.tier}")
    print(f"PRIORITY:          {args.priority}%")
    print(f"STATUS:            {'ACTIVE' if args.active else 'PENDING'}")
    print(f"FILE:              {args.contract}")
    print("-" * 50)
    print("PROCESS COMPLETE")

if __name__ == "__main__":
    main()
