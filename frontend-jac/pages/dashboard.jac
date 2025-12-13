"""
Dashboard Page Component
Main dashboard showing learning progress and quick actions
"""

obj DashboardPage {
    
    can render with entry -> div {
        <div className="dashboard-page">
            {self.render_dashboard_header()}
            {self.render_stats_cards()}
            {self.render_recent_activity()}
            {self.render_recommended_content()}
            {self.render_quick_actions()}
        </div>
    }

    can render_dashboard_header with entry -> div {
        <div className="dashboard-header">
            <h2>📊 Learning Dashboard</h2>
            <p>Welcome back! Here's your learning progress overview.</p>
        </div>
    }

    can render_stats_cards with entry -> div {
        <div className="stats-grid">
            {self.render_stat_card("Concepts Learned", "24", "📚", "#4CAF50")}
            {self.render_stat_card("Current Streak", "7 days", "🔥", "#FF9800")}
            {self.render_stat_card("Mastery Score", "68%", "🎯", "#2196F3")}
            {self.render_stat_card("Time Spent", "24.5h", "⏱️", "#9C27B0")}
        </div>
    }

    can render_stat_card with entry (title: str, value: str, icon: str, color: str) -> div {
        <div className="stat-card" style={`border-left: 4px solid ${color}`}>
            <div className="stat-icon">{icon}</div>
            <div className="stat-content">
                <h3 className="stat-value">{value}</h3>
                <p className="stat-title">{title}</p>
            </div>
        </div>
    }

    can render_recent_activity with entry -> div {
        <div className="dashboard-section">
            <h3>📈 Recent Activity</h3>
            <div className="activity-list">
                {self.render_activity_item("Completed", "Object-Oriented Programming", "2 hours ago")}
                {self.render_activity_item("Started", "Machine Learning Basics", "1 day ago")}
                {self.render_activity_item("Reviewed", "Python Data Structures", "2 days ago")}
                {self.render_activity_item("Achieved", "Week Warrior Badge", "3 days ago")}
            </div>
        </div>
    }

    can render_activity_item with entry (action: str, item: str, time: str) -> div {
        <div className="activity-item">
            <div className="activity-badge">{action}</div>
            <div className="activity-details">
                <span className="activity-item-name">{item}</span>
                <span className="activity-time">{time}</span>
            </div>
        </div>
    }

    can render_recommended_content with entry -> div {
        <div className="dashboard-section">
            <h3>🎯 Recommended for You</h3>
            <div className="recommendation-grid">
                {self.render_recommendation_card(
                    "Next in Path", 
                    "Advanced Python Concepts", 
                    "Continue your Python journey", 
                    "#4CAF50"
                )}
                {self.render_recommendation_card(
                    "Similar Concept", 
                    "Functional Programming", 
                    "Explore alternative paradigms", 
                    "#FF9800"
                )}
                {self.render_recommendation_card(
                    "Review Needed", 
                    "Data Types and Variables", 
                    "Refresh your foundation", 
                    "#F44336"
                )}
            </div>
        </div>
    }

    can render_recommendation_card with entry (type: str, title: str, description: str, color: str) -> div {
        <div className="recommendation-card" style={`border-top: 3px solid ${color}`}>
            <div className="recommendation-header">
                <span className="recommendation-type">{type}</span>
            </div>
            <h4 className="recommendation-title">{title}</h4>
            <p className="recommendation-description">{description}</p>
            <button className="recommendation-cta">Start Learning</button>
        </div>
    }

    can render_quick_actions with entry -> div {
        <div className="dashboard-section">
            <h3>⚡ Quick Actions</h3>
            <div className="quick-actions-grid">
                <button className="quick-action-btn" onClick={() => self.quick_search()}>
                    🔍 Quick Search
                </button>
                <button className="quick-action-btn" onClick={() => self.take_quiz()}>
                    📝 Take Quiz
                </button>
                <button className="quick-action-btn" onClick={() => self.view_progress()}>
                    📊 View Progress
                </button>
                <button className="quick-action-btn" onClick={() => self.browse_concepts()}>
                    📚 Browse Concepts
                </button>
            </div>
        </div>
    }

    # Quick action handlers
    can quick_search with entry {
        print("🔍 Opening quick search...");
        # Navigate to search functionality
    }

    can take_quiz with entry {
        print("📝 Starting quiz...");
        # Navigate to quiz interface
    }

    can view_progress with entry {
        print("📊 Opening progress view...");
        # Navigate to progress page
    }

    can browse_concepts with entry {
        print("📚 Opening concept browser...");
        # Navigate to concepts page
    }
}