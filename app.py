import streamlit as st
import plotly.graph_objects as go
from graph.workflow import build_graph
from market.nifty_tools import get_nifty_index, get_nifty_chart, get_market_leaders

# ===========================================
# PAGE CONFIG & CSS
# ===========================================
st.set_page_config(
    page_title="Financial Intelligence System",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .metric-card { background: #161B22; padding: 15px; border-radius: 12px; border: 1px solid #30363D; box-shadow: 0px 2px 12px rgba(0,0,0,0.3); }
    .big-title { font-size: 40px; font-weight: 700; color: white; }
    .sub-title { color: #A5A5A5; font-size: 18px; margin-bottom: 20px; }
    .section-title { font-size: 28px; font-weight: 600; margin-top: 15px; margin-bottom: 15px; }
    .stock-card { padding: 12px; border-radius: 10px; margin-bottom: 10px; }
    .gainer { background: #16221A; border-left: 6px solid #00C853; }
    .loser { background: #2A1A1A; border-left: 6px solid #FF5252; }
    </style>
    """, unsafe_allow_html=True)

# ===========================================
# DASHBOARD PAGE
# ===========================================
def render_dashboard():
    st.markdown("<div class='big-title'>📈 Multi-Agent Financial Intelligence System</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Enterprise-grade AI-powered Financial Analysis Platform</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Agents", "10", "Active")
    c2.metric("News Sources", "RSS + DDGS")
    c3.metric("Prediction", "LightGBM")
    c4.metric("Market", "NSE")

    st.divider()
    st.markdown("<div class='section-title'>📊 Market Overview</div>", unsafe_allow_html=True)

    try:
        nifty = get_nifty_index()
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("NIFTY 50", f"{nifty['current']:,.2f}", f"{nifty['change']} ({nifty['change_percent']}%)")
        col2.metric("Previous Close", f"{nifty['previous']:,.2f}")
        col3.metric("Market Trend", "Bullish 📈" if nifty["change"] >= 0 else "Bearish 📉")
        col4.metric("Market Sentiment", "Positive" if nifty["change"] >= 0 else "Negative")
    except Exception as e:
        st.warning(f"Unable to fetch NIFTY index data: {e}")

    st.divider()

    left, right = st.columns([2.3, 1])
    
    with left:
        st.markdown("<div class='section-title'>📈 NIFTY 50 Performance</div>", unsafe_allow_html=True)
        chart_period = st.select_slider("Time Period", options=["5d", "1mo", "3mo", "6mo", "1y"], value="1mo")

        try:
            chart = get_nifty_chart(chart_period)
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=chart.index, y=chart["Close"], mode="lines", fill="tozeroy",
                line=dict(width=3, color="#00CC96"),
                hovertemplate="<b>Date</b>: %{x}<br><b>Close</b>: %{y:.2f}<extra></extra>"
            ))
            fig.update_layout(
                template="plotly_dark", height=500, margin=dict(l=15, r=15, t=20, b=15),
                paper_bgcolor="#0E1117", plot_bgcolor="#0E1117", hovermode="x unified",
                yaxis_title="Index", font=dict(size=13)
            )
            fig.update_xaxes(showgrid=False, zeroline=False)
            fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,0.08)", zeroline=False)
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.warning(f"Unable to load chart data: {e}")

    with right:
        st.markdown("<div class='section-title'>🏆 Market Leaders</div>", unsafe_allow_html=True)
        try:
            gainers, losers = get_market_leaders()
            st.markdown("### 🟢 Top Gainers")
            for stock in gainers:
                st.markdown(f"""
                <div class="stock-card gainer">
                    <b>{stock['company']}</b><br>₹ {stock['price']}<br>
                    <span style="color:#00E676">▲ {stock['change']}%</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("### 🔴 Top Losers")
            for stock in losers:
                st.markdown(f"""
                <div class="stock-card loser">
                    <b>{stock['company']}</b><br>₹ {stock['price']}<br>
                    <span style="color:#FF5252">▼ {abs(stock['change'])}%</span>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Unable to load market leaders: {e}")

# ===========================================
# COMPANY ANALYSIS PAGE
# ===========================================
def render_company_analysis(graph):
    st.markdown("<div class='big-title'>🏢 Company Intelligence</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Analyze any company using our Multi-Agent Financial Intelligence Engine.</div>", unsafe_allow_html=True)

    c1, c2 = st.columns([5, 1])
    with c1:
        company = st.text_input("", placeholder="Search company (e.g., Infosys, TCS, Reliance, NVIDIA...)")
    with c2:
        analyze = st.button("🚀 Analyze", use_container_width=True)

    st.divider()

    if analyze:
        if not company.strip():
            st.warning("Please enter a company name.")
            return

        with st.status("Running Financial Intelligence Pipeline...", expanded=True) as status:
            st.write("🧠 Supervisor Agent initialized")
            st.write("🔍 DDGS & 📰 RSS Agents gathering context")
            st.write("📊 Event Extraction & ⚠ Risk Analysis running")
            st.write("🤖 Prediction Agent computing metrics")

            try:
                result = graph.invoke({"query": company})
                status.update(label="Analysis Complete", state="complete", expanded=False)
            except Exception as e:
                status.update(label="Analysis Failed", state="error")
                st.error(f"Pipeline execution failed: {e}")
                return

        # Safely extract dictionary results
        report = result.get("report", "No report generated.")
        events = result.get("events", [])
        sentiment = result.get("sentiment", "Neutral")
        risk = result.get("risk_analysis", "No risk analysis available.")
        prediction = result.get("ml_prediction", {})
        ddgs_news = result.get("ddgs_news", "No DDGS news found.")
        rss_news = result.get("rss_news", "No RSS news found.")

        # Dashboard Output
        st.markdown("## 📊 Company Dashboard")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Events", len(events))
        
        sent_label = "🟢 Positive" if "positive" in sentiment.lower() else "🔴 Negative" if "negative" in sentiment.lower() else "🟡 Neutral"
        m2.metric("Sentiment", sent_label)
        
        m3.metric("Recommendation", prediction.get("recommendation", "N/A") if prediction else "N/A")
        m4.metric("AI Engine", "Gemini")

        st.divider()

        # Prediction & Risk Columns
        left, right = st.columns([1.2, 1])
        with left:
            st.markdown("## 🤖 AI Prediction")
            if prediction:
                p1, p2 = st.columns(2)
                p1.metric("Current Price", f"₹ {prediction.get('current_price', 0)}")
                p1.metric("Direction", prediction.get("direction", "-"))
                p2.metric("Tomorrow", f"₹ {prediction.get('predicted_price', 0)}")
                p2.metric("Confidence", f"{prediction.get('confidence', 0)}%")
                st.metric("Expected Return", f"{prediction.get('predicted_return', 0)}%")

                rec = prediction.get("recommendation", "")
                if rec == "BUY":
                    st.success(f"🟢 Recommendation : **{rec}**")
                elif rec == "SELL":
                    st.error(f"🔴 Recommendation : **{rec}**")
                else:
                    st.warning(f"🟡 Recommendation : **{rec}**")
            else:
                st.info("Prediction metrics unavailable.")

        with right:
            st.markdown("## ⚠ Risk Summary")
            st.markdown(risk)

        st.divider()

        # Deep Dive Tabs
        st.markdown("## 📑 Financial Intelligence Report")
        tab1, tab2, tab3, tab4 = st.tabs(["📄 Report", "📰 News", "📋 Events", "⚠ Risk & Sentiment"])

        with tab1:
            st.markdown(f"<div class='metric-card'>{report}</div>", unsafe_allow_html=True)
            t1, t2, t3 = st.columns(3)
            t1.download_button("⬇ Download Report", report, file_name=f"{company}_report.md", use_container_width=True)
            t2.button("📋 Copy Report", use_container_width=True)
            t3.button("📤 Export PDF", use_container_width=True)

        with tab2:
            st.subheader("📰 Latest Market News")
            st.markdown("### 🔍 DDGS News")
            with st.container(border=True): st.write(ddgs_news)
            st.markdown("### 📰 RSS News")
            with st.container(border=True): st.write(rss_news)

        with tab3:
            st.subheader("📋 Extracted Business Events")
            if not events:
                st.info("No events extracted.")
            else:
                for event in events:
                    impact = event.get("impact", "Neutral")
                    color = "#00C853" if impact.lower() == "positive" else "#F44336" if impact.lower() == "negative" else "#2196F3"
                    st.markdown(f"""
                    <div style="padding:15px; margin-bottom:15px; border-left:6px solid {color}; background:#161B22; border-radius:10px;">
                        <h4>{event.get('title', 'Unknown Title')}</h4>
                        <b>Category:</b> {event.get('category', '-')} <br>
                        <b>Impact:</b> {impact}
                    </div>
                    """, unsafe_allow_html=True)

        with tab4:
            r1, r2 = st.columns(2)
            with r1:
                st.subheader("⚠ Risk Assessment")
                with st.container(border=True): st.markdown(risk)
            with r2:
                st.subheader("😊 Market Sentiment")
                with st.container(border=True): st.markdown(sentiment)

        st.divider()

        # Timeline & System Stats
        st.markdown("<div class='section-title'>⚙ Agent Execution Timeline</div>", unsafe_allow_html=True)
        for step in ["🧠 Supervisor Agent", "🔍 DDGS Search", "📰 RSS Parser", "🔗 News Aggregator", "📊 Event Extraction", "😊 Sentiment Analysis", "⚠ Risk Analysis", "🤖 ML Prediction", "📝 Report Generation"]:
            st.success(f"✔ {step}")

        st.divider()
        st.markdown("<div class='section-title'>📊 System Summary</div>", unsafe_allow_html=True)
        sum1, sum2 = st.columns(2)
        sum1.info(f"### Target\n{company}\n### Data Points\n{len(events)} Events Extracted\n### News Pipelines\nRSS + DDGS")
        sum2.info("### ML Model\nLightGBM\n### Intelligence\nGemini\n### Agent Framework\nLangGraph")

        with st.expander("🛠 View Raw Agent Outputs", expanded=False):
            for key, value in result.items():
                st.markdown(f"### {key}")
                if isinstance(value, (dict, list)):
                    st.json(value)
                else:
                    st.write(value)
                st.divider()

# ===========================================
# MAIN EXECUTION
# ===========================================
def main():
    load_css()
    
    # Initialize your LangGraph workflow
    graph = build_graph()

    st.sidebar.title("📈 Financial Intelligence")
    st.sidebar.markdown("---")
    
    # Using a selectbox is slightly cleaner than radio for navigation
    page = st.sidebar.selectbox("Navigation", ["🏠 Dashboard", "🏢 Company Analysis", "⚙ Workflow Diagnostics"])
    
    st.sidebar.markdown("---")
    st.sidebar.info("### Stack Architecture\n✅ LangGraph\n✅ Gemini\n✅ DuckDuckGo\n✅ RSS Feeds\n✅ Yahoo Finance\n✅ Streamlit")
    st.sidebar.markdown("---")
    st.sidebar.success("System Status : Online")

    # Routing
    if page == "🏠 Dashboard":
        render_dashboard()
    elif page == "🏢 Company Analysis":
        render_company_analysis(graph)
    elif page == "⚙ Workflow Diagnostics":
        st.title("⚙ Workflow Diagnostics")
        st.info("Agent states and intermediate data objects will surface here during execution. Run an analysis in the 'Company Analysis' tab first.")

if __name__ == "__main__":
    main()