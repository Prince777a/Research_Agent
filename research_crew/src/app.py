# # app.py
# from research_crew.crew import ResearchCrew
# import streamlit as st
# import os
# import time


# # Configure page settings
# st.set_page_config(
#     page_title="Research Agent System",
#     page_icon="🔍",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Create output directory if it doesn't exist
# os.makedirs('output', exist_ok=True)

# # Session state initialization
# if 'report_generated' not in st.session_state:
#     st.session_state.report_generated = False

# def main():
#     st.title("Optimising Agent Interaction: Research Driven MultiAgent System")
#     st.markdown("---")
    
#     # User input section
#     with st.container():
#         col_left, col_right = st.columns([3, 1])
#         with col_left:
#             topic = st.text_input(
#                 "Enter research topic:",
#                 placeholder="e.g. Artificial Intelligence in Healthcare",
#                 key="topic_input"
#             )
#         with col_right:
#             st.markdown("")
#             st.markdown("")
#             generate_disabled = not topic or st.session_state.report_generated
            
#             if st.button(
#                 "🚀 Start Research",
#                 disabled=generate_disabled,
#                 use_container_width=True
#             ):
#                 handle_research_request(topic)

#     # Download section
#     if st.session_state.report_generated or os.path.exists('output/report.md'):
#         show_download_section()

# def handle_research_request(topic):
#     """Handle the research request workflow"""
#     with st.status("🔍 **AI Research Team Activation**", expanded=True) as status:
#         try:
#             # Initialize research team
#             st.session_state.report_generated = False
#             research_team = ResearchCrew()
            
#             # Display agent initialization
#             with st.expander("🤖 Agent Deployment", expanded=True):
#                 st.markdown("### Research Team Composition")
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.markdown("#### Senior Data Researcher")
#                     st.caption("Specialized in deep topic investigation and data gathering")
#                 with col2:
#                     st.markdown("#### Reporting Analyst")
#                     st.caption("Expert in analysis and report synthesis")
#                 st.success("Agents successfully initialized with specialized roles!")

#             # Run research process
#             with st.spinner("🚀 Conducting comprehensive research..."):
#                 start_time = time.time()
#                 crew = research_team.crew()
#                 result = crew.kickoff(inputs={'topic': topic})
                
#                 # Save report
#                 with open('output/report.md', 'w') as f:
#                     f.write(result.raw)
                
#                 # Update session state
#                 st.session_state.report_generated = True
#                 elapsed_time = time.time() - start_time

#             # Success message
#             status.update(
#                 label=f"✅ Research Completed in {elapsed_time:.1f}s!",
#                 state="complete",
#                 expanded=False
#             )
#             st.balloons()
            
#         except Exception as e:
#             status.update(label="❌ Research Failed", state="error")
#             st.error(f"System error: {str(e)}")
#             st.session_state.report_generated = False

# def show_download_section():
#     """Display download section after report generation"""
#     st.markdown("---")
#     with st.container():
#         st.subheader("Research Output")
        
#         col1, col2 = st.columns([1, 2])
#         with col1:
#             if os.path.exists('output/report.md'):
#                 with open('output/report.md', "r") as f:
#                     st.download_button(
#                         "📥 Download Full Report",
#                         f.read(),
#                         file_name="research_report.md",
#                         mime="text/markdown",
#                         use_container_width=True
#                     )
#         with col2:
#             if st.button("🔄 New Research", use_container_width=True):
#                 st.session_state.report_generated = False
#                 st.rerun()

# if __name__ == "__main__":
#     main()



# app.py
# from research_crew.crew import ResearchCrew
# import streamlit as st
# import os
# import time

# # Configure page settings
# st.set_page_config(
#     page_title="Research Agent System",
#     page_icon="🔍",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Create output directory if it doesn't exist
# os.makedirs('output', exist_ok=True)

# # Session state initialization
# if 'report_generated' not in st.session_state:
#     st.session_state.report_generated = False

# def main():
#     st.title("Optimising Agent Interaction: Research Driven MultiAgent System")
#     st.markdown("---")
    
#     # User input section
#     with st.container():
#         col_left, col_right = st.columns([3, 1])
#         with col_left:
#             topic = st.text_input(
#                 "Enter research topic:",
#                 placeholder="e.g. Artificial Intelligence in Healthcare",
#                 key="topic_input"
#             )
#         with col_right:
#             st.markdown("")
#             st.markdown("")
#             generate_disabled = not topic or st.session_state.report_generated
            
#             if st.button(
#                 "🚀 Start Research",
#                 disabled=generate_disabled,
#                 use_container_width=True
#             ):
#                 handle_research_request(topic)

#     # Download section
#     if st.session_state.report_generated or os.path.exists('output/report.md'):
#         show_download_section()

# def handle_research_request(topic):
#     """Handle the research request workflow"""
#     with st.status("🔍 **AI Research Team Activation**", expanded=True) as status:
#         try:
#             # Initialize research team
#             st.session_state.report_generated = False
#             research_team = ResearchCrew()
            
#             # Display agent initialization outside the status container
#             st.session_state.agent_info = st.empty()
#             with st.session_state.agent_info.container():
#                 st.markdown("### Research Team Composition")
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.markdown("#### Senior Data Researcher")
#                     st.caption("Specialized in deep topic investigation and data gathering")
#                 with col2:
#                     st.markdown("#### Reporting Analyst")
#                     st.caption("Expert in analysis and report synthesis")
#                 st.success("Agents successfully initialized with specialized roles!")

#             # Run research process
#             with st.spinner("🚀 Conducting comprehensive research..."):
#                 start_time = time.time()
#                 crew = research_team.crew()
#                 result = crew.kickoff(inputs={'topic': topic})
                
#                 # Save report
#                 with open('output/report.md', 'w') as f:
#                     f.write(result.raw)
                
#                 # Update session state
#                 st.session_state.report_generated = True
#                 elapsed_time = time.time() - start_time

#             # Clear agent info after completion
#             st.session_state.agent_info.empty()
            
#             # Success message
#             status.update(
#                 label=f"✅ Research Completed in {elapsed_time:.1f}s!",
#                 state="complete",
#                 expanded=False
#             )
#             st.balloons()
            
#         except Exception as e:
#             status.update(label="❌ Research Failed", state="error")
#             st.error(f"System error: {str(e)}")
#             st.session_state.report_generated = False

# def show_download_section():
#     """Display download section after report generation"""
#     st.markdown("---")
#     with st.container():
#         st.subheader("Research Output")
        
#         col1, col2 = st.columns([1, 2])
#         with col1:
#             if os.path.exists('output/report.md'):
#                 with open('output/report.md', "r") as f:
#                     st.download_button(
#                         "📥 Download Full Report",
#                         f.read(),
#                         file_name="research_report.md",
#                         mime="text/markdown",
#                         use_container_width=True
#                     )
#         with col2:
#             if st.button("🔄 New Research", use_container_width=True):
#                 st.session_state.report_generated = False
#                 st.rerun()

# if __name__ == "__main__":
#     main()

from research_crew.crew import ResearchCrew
import streamlit as st
import os
import time

# Configure page settings
st.set_page_config(
    page_title="Research Agent System",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Session state initialization
if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False

def main():
    st.title("Optimizing Agent Interaction: Research Driven MultiAgent System")
    st.markdown("---")
    
    # Display team composition upfront
    with st.expander("🔬 Meet the Research Team", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Senior Data Researcher")
            st.caption("""
            - Deep topic investigation specialist
            - Academic database navigation
            - Source validation expert
            """)
        with col2:
            st.markdown("### Reporting Analyst")
            st.caption("""
            - Data synthesis professional
            - Technical writing specialist
            - Insight visualization expert
            """)
    
    # User input section
    with st.container():
        topic = st.text_input(
            "Enter research topic:",
            placeholder="e.g. Artificial Intelligence in Healthcare",
            key="topic_input",
            label_visibility="visible"
        )
        
        col1, col2 = st.columns([3, 1])
        with col2:
            st.markdown("")
            generate_disabled = not topic or st.session_state.report_generated
            if st.button(
                "🚀 Start Research",
                disabled=generate_disabled,
                use_container_width=True,
                type="primary"
            ):
                handle_research_request(topic)

    # Download section
    if st.session_state.report_generated or os.path.exists('output/report.md'):
        show_download_section()

def handle_research_request(topic):
    """Handle the research request workflow"""
    with st.status("🔍 **AI Research Team Activation**", expanded=True) as status:
        try:
            # Initialize research team
            st.session_state.report_generated = False
            research_team = ResearchCrew()
            
            # Display research initiation message
            st.toast("Initializing expert agents...", icon="👥")
            with st.container():
                st.success("Research Team Activated!")
                st.write(f"**Research Focus:** {topic}")
            
            # Run research process
            with st.spinner("🚀 Conducting comprehensive research..."):
                start_time = time.time()
                crew = research_team.crew()
                result = crew.kickoff(inputs={'topic': topic})
                
                # Save report
                with open('output/report.md', 'w') as f:
                    f.write(result.raw)
                
                # Update session state
                st.session_state.report_generated = True
                elapsed_time = time.time() - start_time

            # Success message
            status.update(
                label=f"✅ Research Completed in {elapsed_time:.1f}s!",
                state="complete",
                expanded=False
            )
            st.toast("Report generated successfully!", icon="📄")
            st.balloons()
            
        except Exception as e:
            status.update(label="❌ Research Failed", state="error")
            st.error(f"System error: {str(e)}")
            st.session_state.report_generated = False

def show_download_section():
    """Display download section after report generation"""
    st.markdown("---")
    with st.container():
        st.subheader("Research Output")
        
        if os.path.exists('output/report.md'):
            with open('output/report.md', "r") as f:
                report_content = f.read()
                
            col1, col2 = st.columns([1, 1])
            with col1:
                st.download_button(
                    "📥 Download Full Report",
                    report_content,
                    file_name="research_report.md",
                    mime="text/markdown",
                    use_container_width=True,
                    type="primary"
                )
            with col2:
                if st.button(
                    "🔄 New Research",
                    use_container_width=True,
                    help="Start a new research project"
                ):
                    st.session_state.report_generated = False
                    st.rerun()
            
            # Add report preview
            with st.expander("📄 Preview Report Contents", expanded=True):
                st.markdown(report_content)

if __name__ == "__main__":
    main()