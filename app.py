import streamlit as st

from graph.workflow import build_graph

st.set_page_config(
    page_title="Financial Intelligence System",
    page_icon="📈",
    layout="wide"
)

graph = build_graph()

# ----------------------------------
# Header
# ----------------------------------

st.title("📈 Multi-Agent Financial Intelligence System")
st.subheader(
    "🎬 System Walkthrough"
)

with open(
    "Create_a_professional_se.mp4",
    "rb"
) as f:

    st.video(f.read())

st.divider()
st.markdown(
    """
    Analyze companies using a team of AI agents:

    - Supervisor Agent
    - News Agent
    - Filter Agent
    - Event Extraction Agent
    - Risk Agent
    - Sentiment Agent
    - Report Agent
    """
)

st.divider()

# ----------------------------------
# Input
# ----------------------------------

company = st.text_input(
    "Enter Company Name",
    placeholder="NVIDIA"
)

# ----------------------------------
# Analyze Button
# ----------------------------------

if st.button("🚀 Analyze", use_container_width=True):

    if company.strip() == "":
        st.warning("Please enter a company name.")
        st.stop()

    # ----------------------------------
    # Agent Status
    # ----------------------------------

    with st.status(
        "Running Multi-Agent Analysis...",
        expanded=True
    ) as status:

        status.write("🧠 Supervisor Agent")
        status.write("📰 News Agent")
        status.write("🧹 Filter Agent")
        status.write("📊 Event Extraction Agent")
        status.write("⚠️ Risk Agent")
        status.write("😊 Sentiment Agent")
        status.write("📝 Report Agent")

        result = graph.invoke(
            {
                "query": company
            }
        )

        status.update(
            label="Analysis Complete",
            state="complete"
        )

    # ----------------------------------
    # Extract Data
    # ----------------------------------

    events = result.get("events", [])

    risk_analysis = result.get(
        "risk_analysis",
        "Not Available"
    )

    sentiment = result.get(
        "sentiment",
        "Not Available"
    )

    report = result.get(
        "report",
        "Not Available"
    )

    # ----------------------------------
    # Metrics
    # ----------------------------------

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Events Found",
            len(events)
        )

    with col2:
        if "positive" in sentiment.lower():
            st.metric(
                "Sentiment",
                "Positive"
            )
        elif "negative" in sentiment.lower():
            st.metric(
                "Sentiment",
                "Negative"
            )
        else:
            st.metric(
                "Sentiment",
                "Neutral"
            )

    with col3:
        st.metric(
            "Agents",
            "7"
        )

    st.divider()

    # ----------------------------------
    # Tabs
    # ----------------------------------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📄 Report",
            "📊 Events",
            "⚠️ Risk",
            "🔍 Agent Data"
        ]
    )

    # ----------------------------------
    # REPORT TAB
    # ----------------------------------

    with tab1:

        st.subheader("Financial Report")

        st.markdown(report)

    # ----------------------------------
    # EVENTS TAB
    # ----------------------------------

    with tab2:

        st.subheader("Extracted Events")

        if len(events) == 0:

            st.warning(
                "No events extracted."
            )

        else:

            for event in events:

                impact = event.get(
                    "impact",
                    "Unknown"
                )

                title = event.get(
                    "title",
                    "Unknown"
                )

                category = event.get(
                    "category",
                    "Unknown"
                )

                if impact.lower() == "positive":

                    st.success(
                        f"""
                        Event: {title}

                        Category: {category}

                        Impact: {impact}
                        """
                    )

                elif impact.lower() == "negative":

                    st.error(
                        f"""
                        Event: {title}

                        Category: {category}

                        Impact: {impact}
                        """
                    )

                else:

                    st.info(
                        f"""
                        Event: {title}

                        Category: {category}

                        Impact: {impact}
                        """
                    )

    # ----------------------------------
    # RISK TAB
    # ----------------------------------

    with tab3:

        st.subheader(
            "Risk Assessment"
        )

        st.markdown(
            risk_analysis
        )

    # ----------------------------------
    # DEBUG TAB
    # ----------------------------------

    with tab4:

        st.subheader(
            "Raw Agent Output"
        )

        st.json(result)
    st.download_button(
        "Download Report",
        report,
        file_name=f"{company}_report.txt"
    )