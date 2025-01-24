import pandas as pd

def csv_to_html(input_csv, output_html):
    # Read the CSV into a DataFrame
    df = pd.read_csv(input_csv)
    
    # Add CSS for table styling
    style = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-family: Arial, sans-serif;
            font-size: 10px;
        }
        th, td {
            border: 1px solid #ddd;
            text-align: center;
            padding: 1px;
        }
        th {
            background-color: #f4f4f4;
            font-weight: bold;
            cursor: pointer;
            -webkit-user-select: none; /* Safari */        
            -moz-user-select: none; /* Firefox */
            -ms-user-select: none; /* IE10+/Edge */
            user-select: none; /* Standard */
        }
        body {
            font-family: sans-serif;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        caption {
            font-size: 10px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .asc {
            color: red;
        }

        .desc {
            color: green;
        }
    </style>
    """

    # Add JavaScript for making the table sortable
    script = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;
            const compare = (a, b) => isNaN(a) || isNaN(b) ? a.toString().localeCompare(b) : a - b;

            document.querySelectorAll('th').forEach(th => {
                th.addEventListener('click', () => {
                    const table = th.closest('table');
                    const rows = Array.from(table.querySelectorAll('tr')).slice(1); // Exclude the header row
                    const idx = Array.from(th.parentNode.children).indexOf(th);
                    const ascending = !th.classList.contains('asc');
                    
                    rows.sort((rowA, rowB) => compare(
                        getCellValue(ascending ? rowA : rowB, idx),
                        getCellValue(ascending ? rowB : rowA, idx)
                    ));
                    
                    rows.forEach(row => table.appendChild(row));
                    
                    table.querySelectorAll('th').forEach(th => th.classList.remove('asc', 'desc'));
                    th.classList.toggle('asc', ascending);
                    th.classList.toggle('desc', !ascending);
                });
            });
        });
    </script>
    """

    print(script)

    # Convert the DataFrame to an HTML table
    table_html = df.to_html(index=False, classes="season-summary", border=0)

    # Add styling, JavaScript, and table to the HTML
    html = f"""
    <html>
    <head>
        {style}
    </head>
    <body>
        <h1 style="text-align: center;">Season Summary</h1>
        {table_html}
        {script}
    </body>
    </html>
    """

    # Write the HTML to the output file
    with open(output_html, "w") as f:
        f.write(html)

    print(f"HTML file successfully written to {output_html}")

# Example usage
input_csv = "player_season_summary.csv"  # Replace with your CSV file path
output_html = "season_summary.html"  # Replace with desired HTML 

csv_to_html(input_csv,output_html)
