def generate_email_body(articles):
    html_body = """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            /* Reset dan base styles */
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                line-height: 1.6; 
                color: #333;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 20px;
            }
            
            /* Container utama */
            .email-container {
                max-width: 600px;
                margin: 0 auto;
                background: #ffffff;
                border-radius: 15px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                overflow: hidden;
            }
            
            /* Header */
            .header {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                color: white;
                padding: 30px 20px;
                text-align: center;
                position: relative;
                overflow: hidden;
            }
            
            .header::before {
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: repeating-linear-gradient(
                    45deg,
                    transparent,
                    transparent 10px,
                    rgba(255,255,255,0.05) 10px,
                    rgba(255,255,255,0.05) 20px
                );
                animation: shimmer 3s linear infinite;
            }
            
            @keyframes shimmer {
                0% { transform: translateX(-100%); }
                100% { transform: translateX(100%); }
            }
            
            .header h1 {
                font-size: 28px;
                margin-bottom: 10px;
                position: relative;
                z-index: 1;
            }
            
            .header p {
                font-size: 16px;
                opacity: 0.9;
                position: relative;
                z-index: 1;
            }
            
            /* Content area */
            .content {
                padding: 30px 20px;
            }
            
            /* Article cards */
            .article {
                background: #ffffff;
                margin-bottom: 25px;
                border-radius: 12px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.08);
                overflow: hidden;
                transition: all 0.3s ease;
                border: 1px solid #f0f0f0;
            }
            
            .article:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 35px rgba(0,0,0,0.15);
                border-color: #667eea;
            }
            
            .article-image {
                width: 100%;
                height: 200px;
                object-fit: cover;
                transition: transform 0.3s ease;
            }
            
            .article:hover .article-image {
                transform: scale(1.05);
            }
            
            .article-content {
                padding: 20px;
            }
            
            .article-category {
                display: inline-block;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                font-size: 12px;
                font-weight: 600;
                padding: 5px 12px;
                border-radius: 20px;
                margin-bottom: 15px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            .article-title {
                font-size: 20px;
                font-weight: 700;
                margin-bottom: 12px;
                line-height: 1.3;
            }
            
            .article-title a {
                color: #2c3e50;
                text-decoration: none;
                transition: color 0.3s ease;
            }
            
            .article-title a:hover {
                color: #667eea;
            }
            
            .article-meta {
                display: flex;
                align-items: center;
                gap: 15px;
                margin-bottom: 15px;
                font-size: 14px;
                color: #7f8c8d;
            }
            
            .author {
                display: flex;
                align-items: center;
                gap: 8px;
            }
            
            .author::before {
                content: '👤';
                font-size: 14px;
            }
            
            .date {
                display: flex;
                align-items: center;
                gap: 8px;
            }
            
            .date::before {
                content: '📅';
                font-size: 14px;
            }
            
            .article-description {
                color: #5a6c7d;
                line-height: 1.6;
                margin-bottom: 20px;
            }
            
            .read-more {
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                padding: 12px 20px;
                border-radius: 25px;
                text-decoration: none;
                font-weight: 600;
                font-size: 14px;
                transition: all 0.3s ease;
                border: none;
                cursor: pointer;
            }
            
            .read-more:hover {
                transform: translateX(5px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
            
            .read-more::after {
                content: '→';
                transition: transform 0.3s ease;
            }
            
            .read-more:hover::after {
                transform: translateX(3px);
            }
            
            /* Footer */
            .footer {
                background: #f8f9fa;
                padding: 30px 20px;
                text-align: center;
                border-top: 1px solid #e9ecef;
            }
            
            .footer p {
                color: #6c757d;
                font-size: 14px;
                margin-bottom: 15px;
            }
            
            .social-links {
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 20px;
            }
            
            .social-links a {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 40px;
                height: 40px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                border-radius: 50%;
                text-decoration: none;
                transition: all 0.3s ease;
            }
            
            .social-links a:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
            }
            
            /* Responsive design */
            @media (max-width: 480px) {
                .email-container {
                    margin: 10px;
                    border-radius: 10px;
                }
                
                .header {
                    padding: 20px 15px;
                }
                
                .header h1 {
                    font-size: 24px;
                }
                
                .content {
                    padding: 20px 15px;
                }
                
                .article-content {
                    padding: 15px;
                }
                
                .article-title {
                    font-size: 18px;
                }
                
                .article-meta {
                    flex-direction: column;
                    align-items: flex-start;
                    gap: 8px;
                }
            }
            
            /* Loading animation untuk gambar */
            .article-image[src=""] {
                background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
                background-size: 200% 100%;
                animation: loading 1.5s infinite;
            }
            
            @keyframes loading {
                0% { background-position: 200% 0; }
                100% { background-position: -200% 0; }
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <h1>🚀 Daily Tech News</h1>
                <p>Stay updated with the latest technology trends and innovations</p>
            </div>
            
            <div class="content">
    """
    
    # Generate articles
    for i, article in enumerate(articles):
        author = article.get('author') or 'Tech Reporter'
        title = article.get('title') or 'Breaking News'
        description = article.get('description') or 'Stay tuned for more details on this developing story.'
        url = article.get('url') or '#'
        image = article.get('urlToImage') or 'https://via.placeholder.com/600x200/667eea/ffffff?text=Tech+News'
        
        # Kategori berdasarkan kata kunci dalam judul
        category = 'TECH'
        if any(word in title.lower() for word in ['ai', 'artificial intelligence', 'machine learning']):
            category = 'AI'
        elif any(word in title.lower() for word in ['crypto', 'bitcoin', 'blockchain']):
            category = 'CRYPTO'
        elif any(word in title.lower() for word in ['startup', 'funding', 'investment']):
            category = 'STARTUP'
        elif any(word in title.lower() for word in ['mobile', 'app', 'ios', 'android']):
            category = 'MOBILE'
        
        html_body += f'''
                <div class="article">
                    <img src="{image}" alt="Article image" class="article-image" onerror="this.src='https://via.placeholder.com/600x200/667eea/ffffff?text=Tech+News'">
                    <div class="article-content">
                        <span class="article-category">{category}</span>
                        <div class="article-title">
                            <a href="{url}" target="_blank">{title}</a>
                        </div>
                        <div class="article-meta">
                            <span class="author">{author}</span>
                            <span class="date">Today</span>
                        </div>
                        <div class="article-description">
                            {description}
                        </div>
                        <a href="{url}" target="_blank" class="read-more">Read Full Article</a>
                    </div>
                </div>
        '''
    
    html_body += """
            </div>
            
            <div class="footer">
                <p>Thanks for reading! Stay curious and keep learning.</p>
                <p style="font-size: 12px; color: #adb5bd;">
                    You're receiving this because you subscribed to our tech newsletter.
                    <br>
                    <a href="#" style="color: #667eea;">Unsubscribe</a> | 
                    <a href="#" style="color: #667eea;">Update Preferences</a>
                </p>
                <div class="social-links">
                    <a href="#" title="Twitter">🐦</a>
                    <a href="#" title="LinkedIn">💼</a>
                    <a href="#" title="GitHub">💻</a>
                    <a href="#" title="Website">🌐</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_body