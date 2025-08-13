import streamlit as st
from agents.document_analyzer import DocumentAnalyzer
from agents.policy_comparator import PolicyComparator
from agents.recommendation_agent import RecommendationAgent
from utils.security import Security
import os

# Initialize agents
analyzer = DocumentAnalyzer()
comparator = PolicyComparator()
recommender = RecommendationAgent()
security = Security()

st.title("Climate Policy Analysis AI")

# Sidebar for file uploads
st.sidebar.header("Upload Policy Documents")
uploaded_files = st.sidebar.file_uploader(
    "Choose policy documents (PDF, DOCX, TXT)",
    type=['pdf', 'docx', 'txt'],
    accept_multiple_files=True
)

if uploaded_files:
    # Process files
    policy_results = []
    policy_texts = []
    
    for uploaded_file in uploaded_files:
        if not security.validate_file_extension(uploaded_file.name):
            st.error(f"Invalid file type: {uploaded_file.name}")
            continue
        
        # Save temporarily
        file_path = os.path.join("data", "temp", uploaded_file.name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Analyze
        try:
            text = analyzer.extract_text(file_path)
            analysis = analyzer.analyze_policy(text)
            policy_results.append({
                'name': uploaded_file.name,
                'analysis': analysis
            })
            policy_texts.append(text)
            
            st.subheader(f"Analysis for {uploaded_file.name}")
            st.json(analysis)
            
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {str(e)}")
    
    # Compare policies if multiple uploaded
    if len(policy_texts) > 1:
        st.header("Policy Comparison")
        comparison = comparator.compare_policies(policy_texts)
        st.write("Similarity Matrix:")
        st.write(comparison['similarity_matrix'])
        
        st.write(f"Most similar policies: {comparison['most_similar']}")
        st.write(f"Most different policies: {comparison['most_different']}")
        
        # Add similarity to results for recommendations
        for i, res in enumerate(policy_results):
            res['similarity'] = comparison['similarity_matrix'][i].mean()
    
    # Generate recommendations
    if policy_results:
        st.header("Recommendations")
        recommendations = recommender.generate_recommendations(policy_results)
        for rec in recommendations:
            st.write(f"- {rec}")

else:
    st.info("Upload policy documents to begin analysis")