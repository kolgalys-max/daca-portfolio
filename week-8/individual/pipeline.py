"""
pipeline.py
UrbanStyle OÜ — automatiseeritud andmepipeline
Roll D: Automation Script
"""

import logging
import time

from data_fetcher import fetch_sales, fetch_customers
from transform import (
    clean_data,
    calculate_weekly_aggregates,
    calculate_kpis,
    merge_datasets,
)
from visualize_export import (
    create_weekly_chart,
    create_kpi_summary,
    export_results,
)


# Logimise seadistus
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def run_pipeline():
    """Käivitab UrbanStyle andmepipeline'i algusest lõpuni."""

    start_time = time.time()

    try:
        logger.info("Pipeline started")

        # 1. EXTRACT — andmete pärimine Supabase'ist
        logger.info("1/4 Andmete pärimine Supabase'ist...")

        df_sales = fetch_sales()
        df_customers = fetch_customers()

        if df_sales.empty:
            raise ValueError("Müügiandmete päring tagastas tühja DataFrame'i.")

        if df_customers.empty:
            raise ValueError("Kliendiandmete päring tagastas tühja DataFrame'i.")

        logger.info(
            f"Andmed päritud: {len(df_sales)} müügirida, "
            f"{len(df_customers)} kliendirida."
        )

        # 2. TRANSFORM — andmete puhastamine ja töötlemine
        logger.info("2/4 Andmete puhastamine ja töötlemine...")

        df_clean = clean_data(df_sales)

        if df_clean.empty:
            raise ValueError("Pärast puhastamist ei jäänud müügiandmeid alles.")

        df_weekly = calculate_weekly_aggregates(df_clean)
        kpis = calculate_kpis(df_clean)
        df_merged = merge_datasets(df_clean, df_customers)

        # Ühildame Roll B ja Roll C veerunimed
        if "sale_date" in df_weekly.columns and "week" not in df_weekly.columns:
            df_weekly = df_weekly.rename(columns={"sale_date": "week"})

        # Ühildame Roll B ja Roll C KPI võtmenimed
        if "unique_customers" in kpis and "customer_count" not in kpis:
            kpis["customer_count"] = kpis["unique_customers"]

        logger.info("Andmete töötlemine lõpetatud.")

        # 3. VISUALIZE — diagrammide loomine
        logger.info("3/4 Visualiseeringute loomine...")

        fig_weekly = create_weekly_chart(df_weekly)
        fig_kpi = create_kpi_summary(kpis)

        logger.info("Visualiseeringud loodud.")

        # 4. EXPORT — tulemuste salvestamine
        logger.info("4/4 Tulemuste eksportimine...")

        export_results(
            df=df_merged,
            output_dir="output",
            fig_weekly=fig_weekly,
            fig_kpi=fig_kpi,
        )

        elapsed_time = time.time() - start_time

        logger.info(
            f"Pipeline complete: {len(df_merged)} rida töödeldud."
        )
        logger.info(
            f"Kogu täitmisaeg: {elapsed_time:.2f} sekundit."
        )

        print("\nPipeline completed successfully!")
        print(f"Töödeldud ridu: {len(df_merged)}")
        print(f"Täitmisaeg: {elapsed_time:.2f} sekundit")

    except Exception as error:
        logger.error(f"Pipeline failed: {error}")
        print(f"\nPipeline failed: {error}")


if __name__ == "__main__":
    run_pipeline()
