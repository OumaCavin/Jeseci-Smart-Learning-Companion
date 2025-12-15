"""
Jeseci Smart Learning Companion - JAC Frontend
AI-Powered Learning Platform with JAC Runtime Integration
"""

# Import components and services
import "./components" as components;
import "./services" as services;
import "./pages" as pages;

# Main application object
obj LearningCompanionApp {
    # Application state
    has user_state: dict = {};
    has current_page: str = "dashboard";
    has concepts: list = [];
    has learning_paths: list = [];
    has is_authenticated: bool = False;
    
    # API Configuration
    has api_base_url: str = "http://127.0.0.1:8000/api/v1";
    has auth_token: str = "";

    # Entry point for the application
    can init_app with entry {
        print("🚀 Initializing Jeseci Smart Learning Companion...");
        
        # Initialize authentication state
        self.check_auth_status();
        
        # Load initial data
        self.load_initial_data();
        
        # Start the application
        self.render_app();
    }

    # Check authentication status
    can check_auth_status with entry {
        # Check if user has valid session
        local_storage_token = self.get_local_storage("auth_token");
        
        if (local_storage_token) {
            self.auth_token = local_storage_token;
            self.is_authenticated = True;
            print("✅ User authenticated");
        } else {
            print("🔐 User not authenticated");
            self.is_authenticated = False;
        }
    }

    # Load initial data from FastAPI backend
    can load_initial_data with entry {
        if (self.is_authenticated) {
            # Create FastAPI service instance
            api_service = services.FastAPIService();
            api_service.set_auth_token(self.auth_token);
            
            # Load concepts
            concepts_data = api_service.get_concepts();
            self.concepts = concepts_data;
            
            # Load learning paths
            paths_data = api_service.get_learning_paths();
            self.learning_paths = paths_data;
        }
    }

    # Render the main application
    can render_app with entry {
        <div className="learning-companion-app">
            {self.render_header()}
            {self.render_main_content()}
            {self.render_footer()}
        </div>
    }

    # Render application header
    can render_header with entry {
        <header className="app-header">
            <div className="header-content">
                <h1 className="app-title">
                    🎓 Jeseci Smart Learning Companion
                </h1>
                {self.render_navigation()}
            </div>
        </header>
    }

    # Render navigation menu
    can render_navigation with entry {
        <nav className="main-nav">
            <ul className="nav-list">
                <li className="nav-item">
                    <button 
                        className={`nav-link ${self.current_page == 'dashboard' ? 'active' : ''}`}
                        onClick={() => self.navigate_to_page("dashboard")}
                    >
                        📊 Dashboard
                    </button>
                </li>
                <li className="nav-item">
                    <button 
                        className={`nav-link ${self.current_page == 'concepts' ? 'active' : ''}`}
                        onClick={() => self.navigate_to_page("concepts")}
                    >
                        📚 Concepts
                    </button>
                </li>
                <li className="nav-item">
                    <button 
                        className={`nav-link ${self.current_page == 'learning-paths' ? 'active' : ''}`}
                        onClick={() => self.navigate_to_page("learning-paths")}
                    >
                        🛤️ Learning Paths
                    </button>
                </li>
                <li className="nav-item">
                    <button 
                        className={`nav-link ${self.current_page == 'progress' ? 'active' : ''}`}
                        onClick={() => self.navigate_to_page("progress")}
                    >
                        📈 Progress
                    </button>
                </li>
                {self.render_auth_buttons()}
            </ul>
        </nav>
    }

    # Render authentication buttons
    can render_auth_buttons with entry {
        if (self.is_authenticated) {
            <div className="auth-section">
                <span className="user-greeting">Welcome, {self.get_user_name()}</span>
                <button 
                    className="logout-btn"
                    onClick={() => self.logout()}
                >
                    🚪 Logout
                </button>
            </div>
        } else {
            <div className="auth-section">
                <button 
                    className="login-btn"
                    onClick={() => self.show_login_modal()}
                >
                    🔐 Login
                </button>
                <button 
                    className="register-btn"
                    onClick={() => self.show_register_modal()}
                >
                    📝 Register
                </button>
            </div>
        }
    }

    # Render main content area
    can render_main_content with entry {
        <main className="main-content">
            {self.render_current_page()}
        </main>
    }

    # Render current page content
    can render_current_page with entry {
        if (!self.is_authenticated) {
            return self.render_welcome_page();
        }
        
        match (self.current_page) {
            case "dashboard": return pages.DashboardPage.render();
            case "concepts": return pages.ConceptsPage.render(self.concepts);
            case "learning-paths": return pages.LearningPathsPage.render(self.learning_paths);
            case "progress": return pages.ProgressPage.render();
            default: return pages.DashboardPage.render();
        }
    }

    # Render welcome page for unauthenticated users
    can render_welcome_page with entry {
        <div className="welcome-page">
            <div className="welcome-content">
                <h2>Welcome to Jeseci Smart Learning Companion</h2>
                <p>An AI-powered personalized learning platform</p>
                <div className="features-grid">
                    <div className="feature-card">
                        <h3>🎯 Adaptive Learning</h3>
                        <p>Personalized learning paths based on your progress and goals</p>
                    </div>
                    <div className="feature-card">
                        <h3>📊 Progress Tracking</h3>
                        <p>Monitor your learning journey with detailed analytics</p>
                    </div>
                    <div className="feature-card">
                        <h3>🧠 AI-Powered</h3>
                        <p>Smart recommendations and adaptive content delivery</p>
                    </div>
                    <div className="feature-card">
                        <h3>🌐 Knowledge Graph</h3>
                        <p>Explore concepts with intelligent relationship mapping</p>
                    </div>
                </div>
                <div className="cta-buttons">
                    <button className="cta-btn primary" onClick={() => self.show_login_modal()}>
                        Get Started - Login
                    </button>
                    <button className="cta-btn secondary" onClick={() => self.show_register_modal()}>
                        Create Account
                    </button>
                </div>
            </div>
        </div>
    }

    # Render application footer
    can render_footer with entry {
        <footer className="app-footer">
            <div className="footer-content">
                <p>&copy; 2025 Jeseci Smart Learning Companion | Powered by JAC Runtime</p>
                <div className="footer-links">
                    <a href="#about">About</a>
                    <a href="#help">Help</a>
                    <a href="#contact">Contact</a>
                </div>
            </div>
        </footer>
    }

    # Navigation methods
    can navigate_to_page with entry (page_name: str) {
        self.current_page = page_name;
        self.render_app();  # Re-render the application
    }

    # Authentication methods
    can show_login_modal with entry {
        # Pass the app instance to the modal for callback
        components.LoginModal.show(self);
    }

    can show_register_modal with entry {
        # Pass the app instance to the modal for callback
        components.RegisterModal.show(self);
    }
    
    # Handle login from modal
    can handle_modal_login with entry (login_input: str, password: str, remember_me: bool) {
        self.login(login_input, password);
    }
    
    # Handle register from modal
    can handle_modal_register with entry (user_data: dict) {
        self.register(user_data);
    }

    can login with entry (login_input: str, password: str) {
        try {
            # Call FastAPI login endpoint
            login_response = services.FastAPIService.login(login_input, password);
            
            if (login_response["success"]) {
                self.auth_token = login_response["token"];
                self.is_authenticated = True;
                self.save_to_local_storage("auth_token", self.auth_token);
                self.load_initial_data();
                self.render_app();
                print("✅ Login successful");
            } else {
                print(f"❌ Login failed: {login_response.get('error', 'Unknown error')}");
            }
        } catch (error) {
            print(f"❌ Login error: {error}");
        }
    }

    can register with entry (user_data: dict) {
        try {
            # Call FastAPI register endpoint
            register_response = services.FastAPIService.register(user_data);
            
            if (register_response["success"]) {
                print("✅ Registration successful");
                self.show_login_modal();
            } else {
                print(f"❌ Registration failed: {register_response.get('error', 'Unknown error')}");
            }
        } catch (error) {
            print(f"❌ Registration error: {error}");
        }
    }

    can logout with entry {
        self.auth_token = "";
        self.is_authenticated = False;
        self.clear_local_storage("auth_token");
        self.render_app();
        print("👋 Logged out successfully");
    }

    # Utility methods
    can get_user_name with entry {
        # Extract user name from JWT token or user data
        return "Learner";  # Placeholder
    }

    # Local storage helpers
    can save_to_local_storage with entry (key: str, value: str) {
        # Browser localStorage integration
        print(f"Saving to localStorage: {key} = {value}");
    }

    can get_local_storage with entry (key: str) -> str {
        # Browser localStorage integration
        print(f"Getting from localStorage: {key}");
        return "";  # Placeholder
    }

    can clear_local_storage with entry (key: str) {
        # Browser localStorage integration
        print(f"Clearing from localStorage: {key}");
    }
}

# Main application entry
walker main {
    can init with entry {
        # Initialize the learning companion app
        app = LearningCompanionApp();
        app.init_app();
    }
}