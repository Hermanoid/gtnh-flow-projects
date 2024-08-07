output_file_name = ""


while (output_file_name:=input("Name of Output File (q to quit)? : ")) not in ['q', 'Q']:

    more = True
    with open(output_file_name + ".yaml", "w") as f:
        while more == True:
            f.write("- m: " + input("Machine Type? : ") + '\n')
            f.write("  tier: " + input("Tier? : ") + '\n')
            f.write("  I:\n")
            num_inputs = int(input("Num Inputs? : "))
            for i in range(0, num_inputs):
                f.write("    " + input("    Name? : ") + ": " + input("    Amount? : ") + '\n')
            f.write("  O:\n")
            num_outputs = int(input("Num Outputs? : "))
            for i in range(0, num_outputs):
                f.write("    " + input("    Name? : ") + ": " + input("    Amount? : ") + '\n')
            f.write("  eut: " + input("Eut? : ") + '\n')
            f.write("  dur: " + input("Dur? : ") + '\n')

            more = input("More? (y/N)") not in ['n', 'N', '']