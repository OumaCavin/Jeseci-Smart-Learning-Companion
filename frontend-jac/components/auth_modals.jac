"""
Authentication Components
Login and Registration modals for user authentication
"""

obj LoginModal {
    has app_instance: dict = None;
    
    can show with entry (app_instance: dict = None) {
        # Store app instance for callbacks
        self.app_instance = app_instance;
        
        <div className="modal-overlay" onClick={(e) => self.close_modal(e)}>
            <div className="modal-content login-modal" onClick={(e) => e.stopPropagation()}>
                {self.render_modal_header()}
                {self.render_login_form()}
                {self.render_login_footer()}
            </div>
        </div>
    }

    can render_modal_header with entry -> div {
        <div className="modal-header">
            <h2>🔐 Login to Jeseci</h2>
            <button className="modal-close" onClick={() => self.close_modal()}>
                ✕
            </button>
        </div>
    }

    can render_login_form with entry -> div {
        <form className="login-form" onSubmit={(e) => self.handle_login(e)}>
            <div className="form-group">
                <label className="form-label">Email Address</label>
                <input 
                    type="email" 
                    className="form-input" 
                    placeholder="Enter your email"
                    name="email"
                    required
                />
            </div>
            
            <div className="form-group">
                <label className="form-label">Password</label>
                <input 
                    type="password" 
                    className="form-input" 
                    placeholder="Enter your password"
                    name="password"
                    required
                />
            </div>
            
            <div className="form-options">
                <label className="checkbox-label">
                    <input type="checkbox" name="remember_me" />
                    <span className="checkbox-custom"></span>
                    Remember me
                </label>
                <a href="#" className="forgot-password">Forgot password?</a>
            </div>
            
            <button type="submit" className="login-submit-btn">
                🚀 Login
            </button>
        </form>
    }

    can render_login_footer with entry -> div {
        <div className="modal-footer">
            <p>Don't have an account? 
                <a href="#" onClick={() => self.show_register()}>Sign up here</a>
            </p>
        </div>
    }

    can handle_login with entry (event: dict) {
        event.preventDefault();
        
        form_data = new FormData(event.target);
        login_input = form_data.get("email");  # Can be email or username
        password = form_data.get("password");
        remember_me = form_data.get("remember_me") == "on";
        
        print(f"🔐 Attempting login for: {login_input}");
        
        # Call the main app's login method
        # The main app handles FastAPI integration
        self.perform_login(login_input, password, remember_me);
    }

    can perform_login with entry (login_input: str, password: str, remember_me: bool) {
        # Integration with main app
        print(f"Logging in user: {login_input}");
        
        if (self.app_instance) {
            # Call the main app's login method
            self.app_instance.handle_modal_login(login_input, password, remember_me);
        } else {
            print("❌ No app instance available for login");
        }
        
        # Close modal
        self.close_modal();
    }

    can close_modal with entry (event: dict = None) {
        if (event && event.target != event.currentTarget) {
            return;  # Don't close if clicking inside modal
        }
        
        # Remove modal from DOM
        print("🔐 Closing login modal");
    }

    can show_register with entry {
        self.close_modal();
        RegisterModal.show();
    }
}

obj RegisterModal {
    has app_instance: dict = None;
    
    can show with entry (app_instance: dict = None) {
        <div className="modal-overlay" onClick={(e) => self.close_modal(e)}>
            <div className="modal-content register-modal" onClick={(e) => e.stopPropagation()}>
                {self.render_modal_header()}
                {self.render_register_form()}
                {self.render_register_footer()}
            </div>
        </div>
    }

    can render_modal_header with entry -> div {
        <div className="modal-header">
            <h2>📝 Create Account</h2>
            <button className="modal-close" onClick={() => self.close_modal()}>
                ✕
            </button>
        </div>
    }

    can render_register_form with entry -> div {
        <form className="register-form" onSubmit={(e) => self.handle_register(e)}>
            <div className="form-row">
                <div className="form-group">
                    <label className="form-label">First Name</label>
                    <input 
                        type="text" 
                        className="form-input" 
                        placeholder="First name"
                        name="first_name"
                        required
                    />
                </div>
                
                <div className="form-group">
                    <label className="form-label">Last Name</label>
                    <input 
                        type="text" 
                        className="form-input" 
                        placeholder="Last name"
                        name="last_name"
                        required
                    />
                </div>
            </div>
            
            <div className="form-group">
                <label className="form-label">Email Address</label>
                <input 
                    type="email" 
                    className="form-input" 
                    placeholder="Enter your email"
                    name="email"
                    required
                />
            </div>
            
            <div className="form-group">
                <label className="form-label">Password</label>
                <input 
                    type="password" 
                    className="form-input" 
                    placeholder="Create a password"
                    name="password"
                    required
                />
            </div>
            
            <div className="form-group">
                <label className="form-label">Confirm Password</label>
                <input 
                    type="password" 
                    className="form-input" 
                    placeholder="Confirm your password"
                    name="confirm_password"
                    required
                />
            </div>
            
            <div className="form-group">
                <label className="form-label">Learning Goals</label>
                <select className="form-select" name="learning_goals">
                    <option value="">Select your primary goal</option>
                    <option value="career">Career Development</option>
                    <option value="skill">Skill Building</option>
                    <option value="personal">Personal Interest</option>
                    <option value="academic">Academic Study</option>
                </select>
            </div>
            
            <div className="form-options">
                <label className="checkbox-label">
                    <input type="checkbox" name="terms_accepted" required />
                    <span className="checkbox-custom"></span>
                    I agree to the <a href="#" className="terms-link">Terms of Service</a>
                </label>
            </div>
            
            <button type="submit" className="register-submit-btn">
                🚀 Create Account
            </button>
        </form>
    }

    can render_register_footer with entry -> div {
        <div className="modal-footer">
            <p>Already have an account? 
                <a href="#" onClick={() => self.show_login()}>Sign in here</a>
            </p>
        </div>
    }

    can handle_register with entry (event: dict) {
        event.preventDefault();
        
        form_data = new FormData(event.target);
        user_data = {
            "first_name": form_data.get("first_name"),
            "last_name": form_data.get("last_name"),
            "email": form_data.get("email"),
            "password": form_data.get("password"),
            "confirm_password": form_data.get("confirm_password"),
            "learning_goals": form_data.get("learning_goals"),
            "terms_accepted": form_data.get("terms_accepted") == "on"
        };
        
        print(f"📝 Attempting registration for: {user_data.email}");
        
        # Validate passwords match
        if (user_data.password != user_data.confirm_password) {
            print("❌ Passwords do not match");
            return;
        }
        
        # Call the main app's register method
        self.perform_register(user_data);
    }

    can perform_register with entry (user_data: dict) {
        # Integration with main app
        print(f"Registering user: {user_data.email}");
        
        if (self.app_instance) {
            # Call the main app's register method
            self.app_instance.handle_modal_register(user_data);
        } else {
            print("❌ No app instance available for registration");
        }
        
        # Close modal after successful registration
        self.close_modal();
    }

    can close_modal with entry (event: dict = None) {
        if (event && event.target != event.currentTarget) {
            return;  # Don't close if clicking inside modal
        }
        
        # Remove modal from DOM
        print("📝 Closing register modal");
    }

    can show_login with entry {
        self.close_modal();
        LoginModal.show();
    }
}