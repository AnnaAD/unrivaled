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
            font-family: "Roboto", sans-serif;
            font-size: 10px;
            border-radius:15px;
            border: 2px solid #ddd;
        }
        
        th, td {
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
            color:black;
        }
        th:hover {
            text-decoration: underline;
        }
        body {
            font-family: "Roboto", sans-serif;
            background-color:var(--color-black-100);
            color: white;
        }

        h1,h3 {
            font-weight: 100;
        }

        :root {
        --color-unrivaled-test-2: linear-gradient(108deg,#0894ff,#c959dd 34%,#ff2e54 68%,#ff9004);
        --color-unrivaled-test: radial-gradient(50vw circle at top left,rgba(85,44,190,.081) 20%,transparent 100%),radial-gradient(40vw circle at bottom right,rgba(44,102,190,.09) 20%,transparent 100%);
        --color-unrivaled-test-40: linear-gradient(108deg,rgba(8,148,255,.4),rgba(201,89,221,.4) 34%,rgba(255,46,84,.4) 68%,rgba(255,144,4,.4));
        --color-unrivaled: linear-gradient(to bottom right,#5dc3ec,#591a7e);
        --color-unrivaled-50: linear-gradient(to bottom right,rgba(93,195,236,.5),rgba(127,17,224,.5));
        --color-unrivaled-40: linear-gradient(to bottom right,rgba(93,195,236,.4),rgba(127,17,224,.4));
        --color-unrivaled-30: linear-gradient(to bottom right,rgba(93,195,236,.3),rgba(127,17,224,.3));
        --color-unrivaled-20: linear-gradient(to bottom right,rgba(93,195,236,.2),rgba(127,17,224,.2));
        --color-unrivaled-right: linear-gradient(90deg,#5dc3ec,#591a7e);
        --color-unrivaled-radial: radial-gradient(circle at center,rgba(127,17,224,.5) 0%,transparent 70%);
        --color-black-fade: linear-gradient(to bottom left,#17181c,transparent);
        --laces-primary-100: #76b1a1;
        --laces-primary-50: rgba(118,177,161,.5);
        --laces-secondary-100: #c34f54;
        --lunar-owls-primary-100: #40347d;
        --lunar-owls-primary-50: rgba(64,52,125,.5);
        --lunar-owls-secondary-100: #f4e087;
        --mist-primary-100: #063860;
        --mist-primary-50: rgba(6,56,96,.5);
        --mist-secondary-100: #a3d3e7;
        --phantom-primary-100: #000;
        --phantom-primary-50: rgba(0,0,0,.5);
        --phantom-secondary-100: #fff;
        --rose-primary-100: #1b5750;
        --rose-primary-50: rgba(27,87,80,.5);
        --rose-secondary-100: #dda493;
        --vinyl-primary-100: #820234;
        --vinyl-primary-50: rgba(130,2,52,.5);
        --vinyl-secondary-100: #1e9cbf;
        --color-black-100: #17181c;
        --color-black-90: rgba(23,24,28,.9);
        --color-black-60: rgba(23,24,28,.6);
        --color-black-50: rgba(23,24,28,.5);
        --color-black-25: rgba(23,24,28,.25);
        --color-black-20: rgba(23,24,28,.2);
        --color-black-33: rgba(0,0,0,.33);
        --color-white-100: #f4f4f4;
        --color-white-92: hsla(0,0%,96%,.92);
        --color-white-90: hsla(0,0%,96%,.9);
        --color-white-80: hsla(0,0%,96%,.8);
        --color-white-70: hsla(0,0%,96%,.7);
        --color-white-60: hsla(0,0%,96%,.6);
        --color-white-50: hsla(0,0%,96%,.5);
        --color-white-33: hsla(0,0%,96%,.33);
        --color-white-25: hsla(0,0%,96%,.25);
        --color-white-10: hsla(0,0%,96%,.1);
        --color-white-5: hsla(0,0%,96%,.05);
        --color-dark-blue-100: #1d1e26;
        --color-dark-blue-50: rgba(29,30,38,.5);
        --color-grey-100: #212121;
        --color-grey-90: rgba(33,33,33,.9);
        --color-grey-50: rgba(33,33,33,.5);
        --color-light-grey-100: #3a3a3a;
        --color-light-grey-80: rgba(58,58,58,.8);
        --color-light-grey-70: rgba(58,58,58,.7);
        --color-light-grey-60: rgba(58,58,58,.6);
        --color-light-grey-50: rgba(58,58,58,.5);
        --color-light-grey-40: rgba(58,58,58,.4);
        --color-light-grey-25: rgba(58,58,58,.25);
        --color-light-grey-20: rgba(58,58,58,.2);
        --color-light-grey-15: rgba(58,58,58,.15);
        --color-light-grey-10: rgba(58,58,58,.1);
        --color-red-100: #f25c54;
        --color-red-90: rgba(242,92,84,.9);
        --color-red-80: rgba(242,92,84,.8);
        --color-red-50: rgba(242,92,84,.5);
        --color-red-5: rgba(242,92,84,.05);
        --color-light-green-100: #54f293;
        --color-green-100: #7dd23a;
        --color-green-90: rgba(125,210,58,.9);
        --color-green-50: rgba(125,210,58,.5);
        --color-green-40: rgba(125,210,58,.4);
        --color-light-blue-100: #5490ec;
        --color-light-blue-90: rgba(84,144,236,.9);
        --color-light-blue-5: rgba(84,144,236,.05);
        --color-blue-100: #0090ca;
        --color-blue-90: rgba(0,144,202,.9);
        --color-blue-80: rgba(0,144,202,.8);
        --color-blue-50: rgba(0,144,202,.5);
        --color-blue-5: rgba(0,144,202,.05);
        --color-orange-100: #fc4506;
        --color-purple-100: #8502d6;
        --color-purple-10: rgba(133,2,214,.1);
        --color-light-purple-100: #c472fb;
        --color-yellow-100: #cd8923;
        --color-yellow-50: rgba(205,137,35,.5);
        --red-btn: var(--color-red-90);
        --red-btn-hover: var(--color-red-100);
        --grey-btn: var(--color-light-grey-40);
        --grey-btn-hover: var(--color-light-grey-60);
        --white-btn: var(--color-white-100);
        --white-btn-hover: var(--color-white-90);
        --blue-btn: var(--color-blue-100);
        --blue-btn-hover: var(--color-blue-90);
        }
        tr:nth-child(even) {
            background-color: var(--color-light-grey-100);
        }
        tr:hover {
            background: var(--color-unrivaled);
        }
        caption {
            font-size: 10px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        th {
            height: 30px;
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

    import datetime
    # Convert the DataFrame to an HTML table
    table_html = df.to_html(index=False, classes="season-summary", border=0)

    # Add styling, JavaScript, and table to the HTML
    html = f"""
    <html>
    <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
        {style}
    </head>
    <body>
        <h1 style="text-align: center;">&#127936; Unrivaled 2025 Season Summary &#127936; </h1>
        <h3 style="text-align: center;"><i>Last Updated {datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")} </i></h3>
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
output_html = "site/index.html"  # Replace with desired HTML 

csv_to_html(input_csv,output_html)
