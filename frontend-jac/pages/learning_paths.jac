"""
Learning Paths Page Component
Display and manage personalized learning paths
"""

obj LearningPathsPage {
    
    can render with entry (paths_data: list) -> div {
        <div className="learning-paths-page">
            {self.render_paths_header()}
            {self.render_paths_overview()}
            {self.render_paths_grid(paths_data)}
            {self.render_create_path_section()}
        </div>
    }

    can render_paths_header with entry -> div {
        <div className="paths-header">
            <h2>🛤️ Learning Paths</h2>
            <p>Structured journeys to master new skills and concepts</p>
            <div className="path-stats">
                <span className="stat">3 Active Paths</span>
                <span className="stat">67% Overall Progress</span>
            </div>
        </div>
    }

    can render_paths_overview with entry -> div {
        <div className="paths-overview">
            <div className="overview-card">
                <h3>📈 Progress Overview</h3>
                <div className="progress-ring">
                    <svg className="progress-circle" width="120" height="120">
                        <circle className="progress-bg" cx="60" cy="60" r="50" />
                        <circle className="progress-bar" cx="60" cy="60" r="50" />
                    </svg>
                    <div className="progress-text">
                        <span className="progress-percentage">67%</span>
                        <span className="progress-label">Complete</span>
                    </div>
                </div>
            </div>
            
            <div className="overview-card">
                <h3>⏱️ Time Investment</h3>
                <div className="time-stats">
                    <div className="time-item">
                        <span className="time-value">24.5h</span>
                        <span className="time-label">Spent</span>
                    </div>
                    <div className="time-item">
                        <span className="time-value">15.5h</span>
                        <span className="time-label">Remaining</span>
                    </div>
                </div>
            </div>
        </div>
    }

    can render_paths_grid with entry (paths_data: list) -> div {
        <div className="paths-grid">
            {self.render_path_cards(paths_data)}
        </div>
    }

    can render_path_cards with entry (paths_data: list) -> list {
        path_cards = [];
        
        for (path in paths_data) {
            path_cards.append(
                self.render_path_card(path)
            );
        }
        
        return path_cards;
    }

    can render_path_card with entry (path: dict) -> div {
        <div className="path-card">
            {self.render_path_header(path)}
            {self.render_path_body(path)}
            {self.render_path_footer(path)}
        </div>
    }

    can render_path_header with entry (path: dict) -> div {
        <div className="path-header">
            <div className="path-icon">
                {self.get_path_icon(path.get("difficulty", "beginner"))}
            </div>
            <div className="path-info">
                <h3 className="path-title">{path.get("name", "Unknown Path")}</h3>
                <div className="path-meta">
                    <span className="path-difficulty">{path.get("difficulty", "Unknown")}</span>
                    <span className="path-duration">{path.get("estimated_duration", "Unknown")}</span>
                </div>
            </div>
        </div>
    }

    can render_path_body with entry (path: dict) -> div {
        <div className="path-body">
            <p className="path-description">{path.get("description", "No description available")}</p>
            {self.render_path_progress(path)}
            {self.render_path_concepts(path)}
        </div>
    }

    can render_path_progress with entry (path: dict) -> div {
        progress = path.get("progress", 0);
        <div className="path-progress-section">
            <div className="progress-header">
                <span className="progress-label">Progress</span>
                <span className="progress-percentage">{int(progress * 100)}%</span>
            </div>
            <div className="progress-bar-container">
                <div className="progress-bar">
                    <div 
                        className="progress-fill" 
                        style={`width: ${progress * 100}%`}
                    ></div>
                </div>
            </div>
        </div>
    }

    can render_path_concepts with entry (path: dict) -> div {
        concepts_count = path.get("concepts_count", 0);
        completed_count = int(concepts_count * path.get("progress", 0));
        
        <div className="path-concepts">
            <div className="concepts-stats">
                <span className="concepts-completed">{completed_count}</span>
                <span className="concepts-separator">/</span>
                <span className="concepts-total">{concepts_count}</span>
                <span className="concepts-label">concepts</span>
            </div>
            <div className="concepts-breakdown">
                <div className="concept-status completed">Completed</div>
                <div className="concept-status in-progress">In Progress</div>
                <div className="concept-status not-started">Not Started</div>
            </div>
        </div>
    }

    can render_path_footer with entry (path: dict) -> div {
        <div className="path-footer">
            <div className="path-actions">
                <button className="action-btn primary" onClick={() => self.continue_path(path)}>
                    {self.get_continue_button_text(path)}
                </button>
                <button className="action-btn secondary" onClick={() => self.view_path_details(path)}>
                    📋 Details
                </button>
                <button className="action-btn tertiary" onClick={() => self.path_options(path)}>
                    ⋯
                </button>
            </div>
            <div className="path-metadata">
                <span className="last-activity">Last activity: 2 days ago</span>
            </div>
        </div>
    }

    can render_create_path_section with entry -> div {
        <div className="create-path-section">
            <div className="create-path-card">
                <div className="create-path-icon">➕</div>
                <h3>Create Custom Path</h3>
                <p>Design your own learning journey</p>
                <button className="create-path-btn" onClick={() => self.show_create_path_modal()}>
                    Create New Path
                </button>
            </div>
        </div>
    }

    # Utility methods
    can get_path_icon with entry (difficulty: str) -> str {
        match (difficulty.lower()) {
            case "beginner": return "🌱";
            case "intermediate": return "🌿";
            case "advanced": return "🌳";
            default: return "📚";
        }
    }

    can get_continue_button_text with entry (path: dict) -> str {
        progress = path.get("progress", 0);
        if (progress == 0) {
            return "🚀 Start Path";
        } else if (progress < 1) {
            return "▶️ Continue";
        } else {
            return "✅ Completed";
        }
    }

    # Event handlers
    can continue_path with entry (path: dict) {
        print(f"▶️ Continuing path: {path.get('name')}");
        # Navigate to path continuation
    }

    can view_path_details with entry (path: dict) {
        print(f"📋 Viewing details for: {path.get('name')}");
        # Navigate to path details page
    }

    can path_options with entry (path: dict) {
        print(f"⋯ Path options for: {path.get('name')}");
        # Show path options menu
    }

    can show_create_path_modal with entry {
        print("➕ Opening create path modal...");
        # Show create path modal
    }
}