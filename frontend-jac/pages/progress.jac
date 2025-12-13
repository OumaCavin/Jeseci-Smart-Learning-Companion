"""
Progress Page Component
Detailed learning progress tracking and analytics
"""

obj ProgressPage {
    
    can render with entry -> div {
        <div className="progress-page">
            {self.render_progress_header()}
            {self.render_progress_overview()}
            {self.render_detailed_analytics()}
            {self.render_learning_streak()}
            {self.render_achievements_section()}
        </div>
    }

    can render_progress_header with entry -> div {
        <div className="progress-header">
            <h2>📈 Learning Progress</h2>
            <p>Track your learning journey and achievements</p>
            <div className="progress-controls">
                <select className="timeframe-selector" onChange={(e) => self.change_timeframe(e.target.value)}>
                    <option value="7d">Last 7 days</option>
                    <option value="30d">Last 30 days</option>
                    <option value="90d">Last 3 months</option>
                    <option value="1y">Last year</option>
                </select>
                <button className="export-btn" onClick={() => self.export_progress()}>
                    📊 Export
                </button>
            </div>
        </div>
    }

    can render_progress_overview with entry -> div {
        <div className="progress-overview">
            <div className="overview-stats-grid">
                {self.render_overview_stat("Total Concepts", "45", "📚", "#4CAF50")}
                {self.render_overview_stat("Completed", "12", "✅", "#2196F3")}
                {self.render_overview_stat("In Progress", "8", "🔄", "#FF9800")}
                {self.render_overview_stat("Mastery Avg", "68%", "🎯", "#9C27B0")}
            </div>
        </div>
    }

    can render_overview_stat with entry (title: str, value: str, icon: str, color: str) -> div {
        <div className="overview-stat-card" style={`border-top: 3px solid ${color}`}>
            <div className="stat-icon">{icon}</div>
            <div className="stat-content">
                <h3 className="stat-value">{value}</h3>
                <p className="stat-title">{title}</p>
            </div>
        </div>
    }

    can render_detailed_analytics with entry -> div {
        <div className="detailed-analytics">
            <div className="analytics-section">
                <h3>📊 Learning Activity</h3>
                <div className="activity-chart">
                    {self.render_activity_chart()}
                </div>
            </div>
            
            <div className="analytics-section">
                <h3>🎯 Performance Metrics</h3>
                <div className="performance-metrics">
                    {self.render_performance_metric("Mastery Improvement", "+15%", "#4CAF50")}
                    {self.render_performance_metric("Confidence Growth", "+20%", "#2196F3")}
                    {self.render_performance_metric("Engagement Rate", "85%", "#FF9800")}
                    {self.render_performance_metric("Retention Rate", "92%", "#9C27B0")}
                </div>
            </div>
        </div>
    }

    can render_activity_chart with entry -> div {
        <div className="activity-chart-container">
            <div className="chart-bars">
                {self.render_chart_bar("Mon", 45, "#4CAF50")}
                {self.render_chart_bar("Tue", 60, "#2196F3")}
                {self.render_chart_bar("Wed", 30, "#FF9800")}
                {self.render_chart_bar("Thu", 75, "#9C27B0")}
                {self.render_chart_bar("Fri", 55, "#F44336")}
                {self.render_chart_bar("Sat", 40, "#607D8B")}
                {self.render_chart_bar("Sun", 25, "#795548")}
            </div>
            <div className="chart-labels">
                <span>Daily Learning Minutes</span>
            </div>
        </div>
    }

    can render_chart_bar with entry (day: str, minutes: int, color: str) -> div {
        height_percentage = (minutes / 80) * 100;  # Max 80 minutes for scale
        
        <div className="chart-bar-container">
            <div 
                className="chart-bar" 
                style={`height: ${height_percentage}%; background-color: ${color}`}
                title={`${day}: ${minutes} minutes`}
            ></div>
            <div className="chart-bar-label">{day}</div>
        </div>
    }

    can render_performance_metric with entry (label: str, value: str, color: str) -> div {
        <div className="performance-metric" style={`border-left: 3px solid ${color}`}>
            <div className="metric-value">{value}</div>
            <div className="metric-label">{label}</div>
            <div className="metric-trend">↗️</div>
        </div>
    }

    can render_learning_streak with entry -> div {
        <div className="learning-streak-section">
            <h3>🔥 Learning Streak</h3>
            <div className="streak-container">
                <div className="streak-main">
                    <div className="streak-number">7</div>
                    <div className="streak-label">Days</div>
                </div>
                <div className="streak-calendar">
                    {self.render_streak_calendar()}
                </div>
            </div>
            <div className="streak-info">
                <p>Keep it up! You're on a 7-day learning streak.</p>
                <p>Longest streak: 15 days</p>
            </div>
        </div>
    }

    can render_streak_calendar with entry -> div {
        <div className="streak-calendar-grid">
            {self.render_streak_days()}
        </div>
    }

    can render_streak_days with entry -> list {
        days = ["S", "M", "T", "W", "T", "F", "S"];
        streak_data = [True, True, True, False, True, True, True];  # Example data
        
        day_elements = [];
        for (i, day in enumerate(days)) {
            is_active = streak_data[i];
            day_elements.append(
                <div className={`streak-day ${is_active ? 'active' : 'inactive'}`}>
                    {day}
                </div>
            );
        }
        return day_elements;
    }

    can render_achievements_section with entry -> div {
        <div className="achievements-section">
            <h3>🏆 Achievements</h3>
            <div className="achievements-grid">
                {self.render_achievement_card("First Concept", "Completed your first learning concept", "🌟", True)}
                {self.render_achievement_card("Week Warrior", "Maintained a 7-day learning streak", "🔥", True)}
                {self.render_achievement_card("Consistent Learner", "Learned for 30 days straight", "📚", False)}
                {self.render_achievement_card("Knowledge Seeker", "Explored 50 different concepts", "🎯", False)}
                {self.render_achievement_card("Speed Learner", "Completed 5 concepts in one day", "⚡", False)}
                {self.render_achievement_card("Master Apprentice", "Achieved 80%+ mastery in 10 concepts", "👑", False)}
            </div>
        </div>
    }

    can render_achievement_card with entry (title: str, description: str, icon: str, earned: bool) -> div {
        <div className={`achievement-card ${earned ? 'earned' : 'locked'}`}>
            <div className="achievement-icon">{icon}</div>
            <div className="achievement-content">
                <h4 className="achievement-title">{title}</h4>
                <p className="achievement-description">{description}</p>
            </div>
            <div className="achievement-status">
                {earned ? "✅" : "🔒"}
            </div>
        </div>
    }

    # Event handlers
    can change_timeframe with entry (timeframe: str) {
        print(f"📅 Changing timeframe to: {timeframe}");
        # Reload progress data for new timeframe
    }

    can export_progress with entry {
        print("📊 Exporting progress data...");
        # Generate and download progress report
    }
}