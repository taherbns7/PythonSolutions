import json
from datetime import datetime

def transform_data(source_data):
    transformed_data = {
        "Data_Trafic_CPE": []
    }
    
    for item in source_data["Data_Trafic_CPE"]:
        # Prepare the base structure for the current IP address
        base_entry = {
            "IP_Addr": item["IP_Addr"].strip(),
            "Groupe": item["Groupe"].strip(),
            "Trafic_Result": []
        }
        
        for result in item["Trafic_Result"]:
            # Format Date_Time to match the target format
            formatted_date_time = datetime.strptime(result["Date_Time"].strip(), "%Y-%m-%d %H:%M:%S").isoformat() + "Z"
            
            # Create a new result entry
            result_entry = {
                "Date_Time": formatted_date_time,
                "duration": result["duration"],
                "stat": result["stat"]
            }
            
            # Append the result entry to the base entry's Trafic_Result
            base_entry["Trafic_Result"].append(result_entry)
        
        # Append the fully constructed entry to the transformed data
        transformed_data["Data_Trafic_CPE"].append(base_entry)
    
    return transformed_data

# Read the source JSON file
with open('source.json', 'r') as file:
    source_data = json.load(file)

# Transform the data
transformed_data = transform_data(source_data)

# Write the transformed data to a new file
with open('transformed.json', 'w') as file:
    json.dump(transformed_data, file, indent=2)

print('Transformation complete!')
