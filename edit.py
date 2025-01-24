import pandas as pd

# Function to calculate per-season stats
def summarize_season_stats(input_csv, output_csv):
    # Read the input CSV
    df = pd.read_csv(input_csv)
    df = df[df["PLAYERS"] != "TEAM"]

    df = df.dropna()

    
    # Convert numeric columns to appropriate types (ignoring FG, 3PT, and FT initially since they are strings)
    numeric_columns = ["MIN", "REB", "OREB", "DREB", "AST", "STL", "BLK", "TO", "PF", "PTS"]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Separate FG, 3PT, and FT into attempts and makes
    for stat in ["FG", "3PT", "FT"]:
        df[[f"{stat}_MADE", f"{stat}_ATTEMPTS"]] = df[stat].str.split("-", expand=True).astype(float)
    
    # Group by PLAYER_NAME to aggregate stats
    season_summary = df.groupby("PLAYERS").agg(
        GAMES_PLAYED=("PLAYERS", "count"),
        MIN=("MIN", "sum"),
        PTS=("PTS", "sum"),
        REB=("REB", "sum"),
        OREB=("OREB", "sum"),
        DREB=("DREB", "sum"),
        AST=("AST", "sum"),
        STL=("STL", "sum"),
        BLK=("BLK", "sum"),
        TO=("TO", "sum"),
        PF=("PF", "sum"),
        FGM=("FG_MADE", "sum"),
        FGA=("FG_ATTEMPTS", "sum"),
        TPM=("3PT_MADE", "sum"),
        TPA=("3PT_ATTEMPTS", "sum"),
        FTM=("FT_MADE", "sum"),
        FTA=("FT_ATTEMPTS", "sum"),
    ).reset_index()

    
    # Calculate averages and shooting percentages
    season_summary["MPG"] = (season_summary["MIN"] / season_summary["GAMES_PLAYED"]).round(2)
    season_summary["PPG"] = (season_summary["PTS"] / season_summary["GAMES_PLAYED"]).round(2)
    season_summary["RPG"] = (season_summary["REB"] / season_summary["GAMES_PLAYED"]).round(2)
    season_summary["APG"] = (season_summary["AST"] / season_summary["GAMES_PLAYED"]).round(2)
    season_summary["SPG"] = (season_summary["STL"] / season_summary["GAMES_PLAYED"]).round(2)
    season_summary["BPG"] = (season_summary["BLK"] / season_summary["GAMES_PLAYED"]).round(2)
    season_summary["TOPG"] = (season_summary["TO"] / season_summary["GAMES_PLAYED"]).round(2)
    season_summary["FGP"] = (season_summary["FGM"] / season_summary["FGA"] * 100).round(1)
    season_summary["TPP"] = (season_summary["TPM"] / season_summary["TPA"] * 100).round(1)
    season_summary["FTP"] = (season_summary["FTM"] / season_summary["FTA"] * 100).round(1)
    
    # Replace NaN percentages with 0% (e.g., if no attempts were made)
    for col in ["FGP", "TPP", "FTP"]:
        season_summary[col] = season_summary[col].fillna(0)
    
    # Select final columns to output
    final_columns = [
        "PLAYERS", "GAMES_PLAYED", "MIN", "MPG", "PTS", "PPG", 
        "REB", "RPG", "OREB", "DREB", "AST", "APG", "STL", "SPG",
        "BLK", "BPG", "TO", "TOPG", "PF",
        "FGM", "FGA", "FGP",
        "TPM", "TPA", "TPP",
        "FTM", "FTA", "FTP",
    ]
    season_summary = season_summary[final_columns]
    
    # Save to a new CSV file
    season_summary.to_csv(output_csv, index=False)
    print(f"Season summary saved to {output_csv}")


# Example usage
input_csv = "basketball_stats.csv"  # Replace with your input CSV filename
output_csv = "player_season_summary.csv"  # Replace with your desired output CSV filename
summarize_season_stats(input_csv, output_csv)
