from supabase import create_client, Client

def send_bills(billDict):
    url: str = 'https://skjonporupvyogtwnfkl.supabase.co'
    key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNram9ucG9ydXB2eW9ndHduZmtsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NDQ0MTE5NCwiZXhwIjoyMDYwMDE3MTk0fQ.NkXjh4jgKtkXah32Ig8HMnzb8eUaTdtg1wJ7st-KA5E'
    supabase: Client = create_client(url, key)

    row: dict = {}
    rows: list = []

    for billNumber in billDict:
        row = {}
        row['bill_number'] = billNumber
        row['name'] = billDict[billNumber]['title']
        row['bill_type'] = billDict[billNumber]['type']
        row['origin_chamber'] = billDict[billNumber]['originChamber']
        row['congress_number'] = billDict[billNumber]['congressNumber']
        rows.append(row)

    supabase.table('AllBills').insert(rows).execute()

        