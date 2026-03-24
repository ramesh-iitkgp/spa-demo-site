#!/usr/bin/env python3
"""
🚀 DEPLOYMENT SYNC SCRIPT
Automatically copies templates to GitHub deployment folder and pushes to repo
"""

import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

class TemplateDeployer:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.templates_dir = self.project_root / "templates"
        self.deployment_dir = self.project_root / "deployment" / "business-demo-site"
        self.sync_log_file = self.project_root / "deployment" / "sync.log"
        self.business_types = ["cafe", "gym", "salon"]  # Add more as needed
        
    def log(self, message):
        """Log message to console and file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        
        # Append to log file
        with open(self.sync_log_file, "a") as f:
            f.write(log_message + "\n")
    
    def sync_template(self, business_type):
        """Sync single template from templates/ to deployment/"""
        template_src = self.templates_dir / business_type / "index.html"
        deployment_dest = self.deployment_dir / business_type / "demo" / "index.html"
        
        # Verify source exists
        if not template_src.exists():
            self.log(f"❌ ERROR: Template not found: {template_src}")
            return False
        
        # Create deployment directory if doesn't exist
        deployment_dest.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy file
        try:
            shutil.copy2(template_src, deployment_dest)
            self.log(f"✅ Synced: {business_type}/index.html")
            return True
        except Exception as e:
            self.log(f"❌ ERROR syncing {business_type}: {str(e)}")
            return False
    
    def sync_all_templates(self):
        """Sync all templates"""
        self.log("🔄 Starting template sync...")
        results = {}
        
        for business_type in self.business_types:
            results[business_type] = self.sync_template(business_type)
        
        synced_count = sum(1 for v in results.values() if v)
        self.log(f"✅ Synced {synced_count}/{len(self.business_types)} templates")
        return all(results.values())
    
    def git_commit_push(self, message="Update templates via sync script"):
        """Commit changes to Git and push to GitHub"""
        try:
            os.chdir(self.deployment_dir.parent.parent)  # Go to repo root
            
            # Add files
            subprocess.run(["git", "add", "."], check=True, capture_output=True)
            
            # Check if there are changes
            status = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
            if not status.stdout.strip():
                self.log("ℹ️  No changes to commit")
                return True
            
            # Commit
            subprocess.run(["git", "commit", "-m", message], check=True, capture_output=True)
            self.log(f"✅ Committed: {message}")
            
            # Push
            result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
            if result.returncode == 0:
                self.log("✅ Pushed to GitHub")
                return True
            else:
                self.log(f"❌ Push failed: {result.stderr}")
                return False
                
        except subprocess.CalledProcessError as e:
            self.log(f"❌ Git error: {str(e)}")
            return False
        except Exception as e:
            self.log(f"❌ ERROR: {str(e)}")
            return False
    
    def validate_templates(self):
        """Validate all templates have required IDs"""
        self.log("🔍 Validating template structure...")
        required_ids = ["pageTitle", "navBrand", "heroTitle", "heroDescription", "locationInfo"]
        
        issues = []
        for business_type in self.business_types:
            template_file = self.templates_dir / business_type / "index.html"
            
            if not template_file.exists():
                issues.append(f"Missing: {business_type}/index.html")
                continue
            
            content = template_file.read_text()
            missing_ids = [id for id in required_ids if f'id="{id}"' not in content]
            
            if missing_ids:
                issues.append(f"{business_type}: Missing IDs: {', '.join(missing_ids)}")
        
        if issues:
            for issue in issues:
                self.log(f"⚠️  {issue}")
            return False
        else:
            self.log("✅ All templates valid")
            return True
    
    def deploy(self, validate=True, git_push=True):
        """Full deployment process"""
        self.log("=" * 60)
        self.log("🚀 DEPLOYMENT STARTED")
        self.log("=" * 60)
        
        # Validate
        if validate:
            if not self.validate_templates():
                self.log("⚠️  Validation warnings detected (continuing...)")
        
        # Sync
        if not self.sync_all_templates():
            self.log("❌ DEPLOYMENT FAILED during sync")
            return False
        
        # Push to GitHub
        if git_push:
            if not self.git_commit_push("Auto-deploy: Update templates"):
                self.log("⚠️  Sync completed but GitHub push failed")
                return False
        
        self.log("=" * 60)
        self.log("✅ DEPLOYMENT COMPLETE")
        self.log("=" * 60)
        return True


# ============================================================================
# USAGE
# ============================================================================

if __name__ == "__main__":
    import sys
    
    # Get project root (adjust if needed)
    project_root = Path(__file__).parent.parent.parent
    
    deployer = TemplateDeployer(project_root)
    
    # Parse arguments
    validate = "--no-validate" not in sys.argv
    git_push = "--no-push" not in sys.argv
    
    # Run deployment
    success = deployer.deploy(validate=validate, git_push=git_push)
    
    sys.exit(0 if success else 1)
