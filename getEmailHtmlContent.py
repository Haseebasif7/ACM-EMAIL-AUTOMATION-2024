def getEmailHtmlContent(name):
  background_image_url = 'https://drive.google.com/uc?export=view&id=1XRpg-Sc-2YJLAaseX3J2yTD-2Vf5GAaA'
  
  return f"""
            <!DOCTYPE html>
            <html>
            <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                width: 80%;
                max-width: 500px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                border: 5px solid rgb(13, 95, 145);
                border-radius: 5px;
                }}
                .email-header {{
                    padding: 10px;
                    text-align: center;
                    color: rgb(0, 0, 0);
                }}
                .email-body {{
                    padding: 20px;
                }}
                .email-body h2 {{
                    color: black;
                }}
                .email-footer {{
                    text-align: center;
                    font-size: 12px;
                    color: #999;
                    padding: 20px 0;
                    border-top: 1px solid #e0e0e0;
                }}
                .email-footer a {{
                    text-decoration: none;
                }}
                
            </style> 
            </head>

            <body>
                <div class="email-container">
                    <div class="email-header">
                        <img src="{background_image_url}" style="width: 50%; border-radius:10px;" alt="ACM Logo">
                        <h1>WELCOME TO NUCES KHI ACM'24-25</h1>
                    </div>

                    <!-- Body -->
                    <div class="email-body">
                        <p>Dear {name},</p>
                        <p>
                            On behalf of the entire executive committee of ACM’24-25, I would like to extend my sincerest congratulations for being selected into our extended executive committee. We are thrilled to have you on board and look forward to your continued contributions in this esteemed position.
                        </p>
                        
                    </div>

                    <div class="email-footer">
                        <p>Best Regards,<br>Hassaan Gatta,<br>President,<br>NUCES KHI ACM Student Chapter</p>
                    </div>
                </div>
            </body>
            </html>
        """