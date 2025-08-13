class RecommendationAgent:
    def generate_recommendations(self, analysis_results):
        recommendations = []
        
        # Simple rule-based recommendations
        for policy in analysis_results:
            targets = policy.get('targets', [])
            if not targets:
                recommendations.append(f"Policy '{policy['name']}': Consider adding specific emission reduction targets")
            else:
                recommendations.append(f"Policy '{policy['name']}': Targets found - {', '.join(targets)}")
        
        # Compare policy similarities
        if len(analysis_results) > 1:
            similarities = [res['similarity'] for res in analysis_results if 'similarity' in res]
            if similarities and max(similarities) > 0.8:
                recommendations.append("Some policies are very similar - consider merging or removing duplicates")
        
        return recommendations