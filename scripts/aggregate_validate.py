import os
import json
import hashlib

## This file seems to have smart content. Note to self. Copy the idea! #-NtS-#
## #-NtS-# means note to self. Easier to find with tags.

DATA_RAW_DIR = '../data/raw'
DATA_VALIDATED_DIR = '../data/validated'
DATA_AGGREGATED_DIR = '../data/aggregated'

def calculate_checksum(data):
    """Calculates a SHA256 checksum for the given data."""
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode('utf-8')).hexdigest()

def load_results(filepath):
    """Loads calculation results from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filepath}")
        return None
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

def save_results(filepath, data):
    """Saves calculation results to a JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def validate_and_aggregate():
    """Validates and aggregates calculation results from the raw data directory."""
    print("Starting data validation and aggregation...")

    raw_files = [f for f in os.listdir(DATA_RAW_DIR) if f.endswith('.json')]
    if not raw_files:
        print("No raw data files found to process.")
        return

    # Group results by task ID for validation
    tasks = {}
    for filename in raw_files:
        filepath = os.path.join(DATA_RAW_DIR, filename)
        result = load_results(filepath)
        if result and 'task_id' in result and 'result' in result:
            task_id = result['task_id']
            if task_id not in tasks:
                tasks[task_id] = []
            tasks[task_id].append({'filename': filename, 'result': result['result'], 'checksum': calculate_checksum(result['result'])})

    validated_results = []
    aggregated_map = {}

    for task_id, submissions in tasks.items():
        if len(submissions) < 2: # Need at least two submissions to validate
            print(f"Skipping task {task_id}: Not enough submissions for validation ({len(submissions)} found).")
            continue

        # Check for consistency among submissions
        first_checksum = submissions[0]['checksum']
        is_consistent = all(s['checksum'] == first_checksum for s in submissions)

        if is_consistent:
            print(f"Task {task_id} is consistent. Validating and aggregating.")
            # Assuming the first result is representative if consistent
            validated_data = {
                'task_id': task_id,
                'result': submissions[0]['result'],
                'validated_by_files': [s['filename'] for s in submissions]
            }
            validated_results.append(validated_data)
            save_results(os.path.join(DATA_VALIDATED_DIR, f'task_{task_id}.json'), validated_data)
            aggregated_map[task_id] = submissions[0]['result']
        else:
            print(f"Task {task_id} is inconsistent. Needs re-calculation.")
            # Optionally, move inconsistent files to a 'recalculate' directory

    # Save the aggregated map
    if aggregated_map:
        save_results(os.path.join(DATA_AGGREGATED_DIR, 'omaha_preflop_equities_map.json'), aggregated_map)
        print(f"Aggregated {len(aggregated_map)} unique tasks into {os.path.join(DATA_AGGREGATED_DIR, 'omaha_preflop_equities_map.json')}")
    else:
        print("No tasks were successfully validated and aggregated.")

    print("Data validation and aggregation complete.")

if __name__ == '__main__':
    # Create dummy raw data for testing
    os.makedirs(DATA_RAW_DIR, exist_ok=True)
    os.makedirs(DATA_VALIDATED_DIR, exist_ok=True)
    os.makedirs(DATA_AGGREGATED_DIR, exist_ok=True)

    # Consistent tasks
    save_results(os.path.join(DATA_RAW_DIR, 'calc_A_user1.json'), {'task_id': 'task_001', 'result': {'hand': 'AAxx', 'equity': 0.65}})
    save_results(os.path.join(DATA_RAW_DIR, 'calc_A_user2.json'), {'task_id': 'task_001', 'result': {'hand': 'AAxx', 'equity': 0.65}})

    save_results(os.path.join(DATA_RAW_DIR, 'calc_B_user1.json'), {'task_id': 'task_002', 'result': {'hand': 'KKxx', 'equity': 0.60}})
    save_results(os.path.join(DATA_RAW_DIR, 'calc_B_user2.json'), {'task_id': 'task_002', 'result': {'hand': 'KKxx', 'equity': 0.60}})

    # Inconsistent task (simulating the 20% error)
    save_results(os.path.join(DATA_RAW_DIR, 'calc_C_user1.json'), {'task_id': 'task_003', 'result': {'hand': 'QQxx', 'equity': 0.55}})
    save_results(os.path.join(DATA_RAW_DIR, 'calc_C_user2.json'), {'task_id': 'task_003', 'result': {'hand': 'QQxx', 'equity': 0.50}})

    # Single submission (should be skipped for validation)
    save_results(os.path.join(DATA_RAW_DIR, 'calc_D_user1.json'), {'task_id': 'task_004', 'result': {'hand': 'JJxx', 'equity': 0.58}})

    validate_and_aggregate()
