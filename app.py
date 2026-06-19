
import streamlit as st
from graph.workflow import build_graph

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Financial Intelligence System",
    page_icon="📈",
    layout="wide"
)

graph = build_graph()

# =====================================================
# HEADER
# =====================================================

st.title("📈 Multi-Agent Financial Intelligence System")

st.markdown("""
AI-powered financial intelligence platform using:

- LangGraph
- Gemini
- DuckDuckGo Search
- RSS Feeds
- Streamlit
""")

st.markdown("""
### Agent Workflow

🧠 Supervisor Agent  
🔍 DDGS Agent  
📰 RSS Agent  
🔗 News Aggregator Agent  
🧹 Filter Agent  
📊 Event Extraction Agent  
⚠️ Risk Agent  
😊 Sentiment Agent  
📝 Report Agent
""")

# =====================================================
# VIDEO SECTION
# =====================================================

try:
    st.subheader("🎬 Project Architecture Overview")

    with open("assets/project_demo.mp4", "rb") as video_file:
        video_bytes = video_file.read()

    st.video(video_bytes)

except:
    st.info("Place your video at: assets/project_demo.mp4")

st.divider()

# =====================================================
# INPUT
# =====================================================

company = st.text_input(
    "Enter Company Name",
    placeholder="Infosys"
)

analyze = st.button(
    "🚀 Analyze Company",
    use_container_width=True
)

# =====================================================
# ANALYSIS
# =====================================================

if analyze:

    if not company.strip():
        st.warning("Please enter a company name.")
        st.stop()

    with st.status(
        "Running Multi-Agent Workflow...",
        expanded=True
    ) as status:

        status.write("🧠 Supervisor Agent")
        status.write("🔍 DDGS Agent")
        status.write("📰 RSS Agent")
        status.write("🔗 News Aggregator Agent")
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

    # =====================================================
    # EXTRACT DATA
    # =====================================================

    report = result.get("report", "")

    sentiment = result.get("sentiment", "")

    risk_analysis = result.get(
        "risk_analysis",
        ""
    )

    events = result.get(
        "events",
        []
    )

    ddgs_news = result.get(
        "ddgs_news",
        ""
    )

    rss_news = result.get(
        "rss_news",
        ""
    )

    filtered_news = result.get(
        "filtered_news",
        ""
    )

    # =====================================================
    # METRICS
    # =====================================================

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Events Extracted",
            len(events)
        )

    with col2:
        st.metric(
            "Agents",
            "9"
        )

    with col3:
        st.metric(
            "News Sources",
            "DDGS + RSS"
        )

    with col4:

        sentiment_text = sentiment.lower()

        if "positive" in sentiment_text:
            st.metric(
                "Sentiment",
                "Positive"
            )

        elif "negative" in sentiment_text:
            st.metric(
                "Sentiment",
                "Negative"
            )

        else:
            st.metric(
                "Sentiment",
                "Neutral"
            )

    st.divider()

    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "📄 Report",
            "📰 News Sources",
            "📋 Events",
            "⚠️ Risk",
            "😊 Sentiment",
            "🤖 Agent Outputs"
        ]
    )

    # =====================================================
    # REPORT
    # =====================================================

    with tab1:

        st.subheader(
            "Financial Intelligence Report"
        )

        st.markdown(report)

        st.download_button(
            label="⬇ Download Report",
            data=report,
            file_name=f"{company}_report.md",
            mime="text/plain"
        )

    # =====================================================
    # NEWS
    # =====================================================

    with tab2:

        st.subheader(
            "🔍 DDGS News"
        )

        st.text(ddgs_news)

        st.divider()

        st.subheader(
            "📰 RSS News"
        )

        st.text(rss_news)

    # =====================================================
    # EVENTS
    # =====================================================

    with tab3:

        st.subheader(
            "Extracted Business Events"
        )

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

                with st.container():

                    if impact.lower() == "positive":

                        st.success(
                            f"""
                            **{title}**

                            Category: {category}

                            Impact: {impact}
                            """
                        )

                    elif impact.lower() == "negative":

                        st.error(
                            f"""
                            **{title}**

                            Category: {category}

                            Impact: {impact}
                            """
                        )

                    else:

                        st.info(
                            f"""
                            **{title}**

                            Category: {category}

                            Impact: {impact}
                            """
                        )

    # =====================================================
    # RISK
    # =====================================================

    with tab4:

        st.subheader(
            "Risk Assessment"
        )

        st.markdown(
            risk_analysis
        )

    # =====================================================
    # SENTIMENT
    # =====================================================

    with tab5:

        st.subheader(
            "Sentiment Analysis"
        )

        st.markdown(
            sentiment
        )

    # =====================================================
    # AGENTS
    # =====================================================

    with tab6:

        with st.expander(
            "🔍 DDGS Agent"
        ):
            st.write(ddgs_news)

        with st.expander(
            "📰 RSS Agent"
        ):
            st.write(rss_news)

        with st.expander(
            "🧹 Filter Agent"
        ):
            st.write(filtered_news)

        with st.expander(
            "📊 Event Extraction Agent"
        ):
            st.json(events)

        with st.expander(
            "⚠️ Risk Agent"
        ):
            st.write(risk_analysis)

        with st.expander(
            "😊 Sentiment Agent"
        ):
            st.write(sentiment)

        with st.expander(
            "📝 Report Agent"
        ):
            st.write(report)

        with st.expander(
            "🗂 Complete State"
        ):
            st.json(result)

