import csv

ENROLLMENTS_FILENAME = 'enrollments.csv'
ENGAGEMENTS_FILENAME = 'daily_engagement_full.csv'
SUBMISSIONS_FILENAME = 'project_submissions.csv'

def extract_csv_data(csv_filename: str) -> list[list]:
    """Given a csv filename, we extract the data into a
    list[list] object."""

    with open(csv_filename, 'r') as f:
        reader = csv.DictReader(f)
        result = list(reader)
    
    return result


if __name__ == "__main__":
    
    print(extract_csv_data(ENROLLMENTS_FILENAME))
    print(extract_csv_data(ENGAGEMENTS_FILENAME))
    print(extract_csv_data(SUBMISSIONS_FILENAME))