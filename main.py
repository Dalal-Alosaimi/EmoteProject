<!DOCTYPE html>
<html lang = "ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emote - تحليل مشاعر الحشود</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800&display=swap');
        
        :root {
            --primary: #2e4ead;
            --secondary: #6c63ff;
            --accent: #ff6b6b;
            --light: #f8f9fa;
            --dark: #212529;
            --success: #28a745;
            --info: #17a2b8;
            --warning: #ffc107;
            --danger: #dc3545;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Tajawal', sans-serif;
            line-height: 1.6;
            color: var(--dark);
            background-color: #f5f7ff;
            overflow-x: hidden;
        }
        
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Header Styles */
        header {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }
        
        .logo {
            font-size: 2rem;
            font-weight: 800;
            color: var(--primary);
            text-decoration: none;
            display: flex;
            align-items: center;
        }
        
        .logo i {
            margin-left: 10px;
            color: var(--accent);
        }
        
        .nav-links {
            display: flex;
            list-style: none;
        }
        
        .nav-links li {
            margin-right: 30px;
        }
        
        .nav-links a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: var(--primary);
        }
        
        .cta-button {
            background-color: var(--primary);
            color: white;
            padding: 10px 20px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 500;
            transition: background-color 0.3s;
        }
        
        .cta-button:hover {
            background-color: var(--secondary);
        }
        
        .menu-toggle {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            padding: 150px 0 100px;
            text-align: center;
        }
        
        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 20px;
            font-weight: 800;
        }
        
        .hero p {
            font-size: 1.2rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }
        
        .hero-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        
        .hero-buttons .cta-button {
            padding: 15px 30px;
            font-size: 1.1rem;
        }
        
        .secondary-button {
            background-color: transparent;
            color: white;
            padding: 15px 30px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 500;
            border: 2px solid white;
            font-size: 1.1rem;
            transition: all 0.3s;
        }
        
        .secondary-button:hover {
            background-color: white;
            color: var(--primary);
        }
        
        /* About Section */
        .about {
            padding: 100px 0;
            background-color: white;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 60px;
        }
        
        .section-title h2 {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 15px;
        }
        
        .section-title p {
            font-size: 1.1rem;
            color: #6c757d;
            max-width: 700px;
            margin: 0 auto;
        }
        
        .about-content {
            display: flex;
            align-items: center;
            gap: 50px;
        }
        
        .about-image {
            flex: 1;
            position: relative;
        }
        
        .about-image-main {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }
        
        .about-text {
            flex: 1;
        }
        
        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--primary);
        }
        
        .about-text p {
            margin-bottom: 20px;
            font-size: 1.05rem;
        }
        
        .feature-list {
            list-style: none;
            margin-top: 30px;
        }
        
        .feature-list li {
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }
        
        .feature-list i {
            color: var(--success);
            margin-left: 15px;
            font-size: 1.2rem;
        }
        
        /* Features Section */
        .features {
            padding: 100px 0;
            background-color: #f8f9fa;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-top: 50px;
        }
        
        .feature-card {
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        }
        
        .feature-icon {
            width: 70px;
            height: 70px;
            background-color: var(--light);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            color: var(--primary);
            font-size: 1.8rem;
        }
        
        .feature-card h3 {
            font-size: 1.4rem;
            margin-bottom: 15px;
            color: var(--dark);
        }
        
        .feature-card p {
            color: #6c757d;
            font-size: 1rem;
        }
        
        /* Technology Section */
        .technology {
            padding: 100px 0;
            background-color: white;
        }
        
        .tech-tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 50px;
            flex-wrap: wrap;
        }
        
        .tech-tab {
            padding: 15px 25px;
            background-color: var(--light);
            border: none;
            margin: 0 10px 10px;
            border-radius: 30px;
            cursor: pointer;
            font-family: 'Tajawal', sans-serif;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.3s;
        }
        
        .tech-tab.active {
            background-color: var(--primary);
            color: white;
        }
        
        .tech-content {
            display: none;
        }
        
        .tech-content.active {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .tech-content-inner {
            display: flex;
            align-items: center;
            gap: 50px;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        .tech-image {
            flex: 1;
        }
        
        .tech-image img {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }
        
        .tech-details {
            flex: 1;
        }
        
        .tech-details h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--primary);
        }
        
        .tech-details p {
            margin-bottom: 20px;
            font-size: 1.05rem;
        }
        
        .tech-list {
            list-style: none;
        }
        
        .tech-list li {
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }
        
        .tech-list i {
            color: var(--primary);
            margin-left: 15px;
            font-size: 1.2rem;
        }
        
        /* Dashboard Preview */
        .dashboard-preview {
            padding: 100px 0;
            background-color: #f8f9fa;
            text-align: center;
        }
        
        .dashboard-image {
            max-width: 1000px;
            margin: 50px auto 0;
            position: relative;
        }
        
        .dashboard-image img {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
        }
        
        .dashboard-features {
            display: flex;
            justify-content: space-between;
            margin-top: 50px;
            flex-wrap: wrap;
        }
        
        .dashboard-feature {
            flex: 1;
            min-width: 250px;
            margin: 20px;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
        }
        
        .dashboard-feature i {
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 15px;
        }
        
        .dashboard-feature h3 {
            font-size: 1.3rem;
            margin-bottom: 10px;
        }
        
        .dashboard-feature p {
            color: #6c757d;
            font-size: 0.95rem;
        }
        
        /* Team Section */
        .team {
            padding: 100px 0;
            background-color: white;
        }
        
        .team-members {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 50px;
            flex-wrap: wrap;
        }
        
        .team-member {
            background-color: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            width: 300px;
            transition: transform 0.3s;
        }
        
        .team-member:hover {
            transform: translateY(-10px);
        }
        
        .member-image {
            height: 300px;
            overflow: hidden;
        }
        
        .member-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }
        
        .team-member:hover .member-image img {
            transform: scale(1.05);
        }
        
        .member-info {
            padding: 20px;
            text-align: center;
        }
        
        .member-info h3 {
            font-size: 1.3rem;
            margin-bottom: 5px;
        }
        
        .member-info p {
            color: #6c757d;
            margin-bottom: 15px;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 15px;
        }
        
        .social-links a {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            background-color: var(--light);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            transition: all 0.3s;
        }
        
        .social-links a:hover {
            background-color: var(--primary);
            color: white;
        }
        
        /* Contact Section */
        .contact {
            padding: 100px 0;
            background-color: #f8f9fa;
        }
        
        .contact-container {
            display: flex;
            gap: 50px;
            margin-top: 50px;
        }
        
        .contact-info {
            flex: 1;
        }
        
        .contact-info h3 {
            font-size: 1.8rem;
            margin-bottom: 30px;
            color: var(--primary);
        }
        
        .contact-details {
            list-style: none;
        }
        
        .contact-details li {
            margin-bottom: 20px;
            display: flex;
            align-items: flex-start;
        }
        
        .contact-details i {
            margin-left: 15px;
            font-size: 1.2rem;
            color: var(--primary);
            margin-top: 5px;
        }
        
        .contact-details strong {
            display: block;
            margin-bottom: 5px;
        }
        
        .contact-form {
            flex: 1;
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        .form-control {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-family: 'Tajawal', sans-serif;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        
        .form-control:focus {
            border-color: var(--primary);
            outline: none;
        }
        
        textarea.form-control {
            min-height: 120px;
            resize: vertical;
        }
        
        .submit-btn {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 30px;
            font-family: 'Tajawal', sans-serif;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .submit-btn:hover {
            background-color: var(--secondary);
        }
        
        /* Footer */
        footer {
            background-color: var(--dark);
            color: white;
            padding: 70px 0 20px;
        }
        
        .footer-content {
            display: flex;
            flex-wrap: wrap;
            gap: 50px;
            margin-bottom: 50px;
        }
        
        .footer-column {
            flex: 1;
            min-width: 200px;
        }
        
        .footer-column h3 {
            font-size: 1.3rem;
            margin-bottom: 20px;
            color: white;
        }
        
        .footer-links {
            list-style: none;
        }
        
        .footer-links li {
            margin-bottom: 10px;
        }
        
        .footer-links a {
            color: rgba(255, 255, 255, 0.7);
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-links a:hover {
            color: white;
        }
        
        .footer-social {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }
        
        .footer-social a {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: rgba(255, 255, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            transition: background-color 0.3s;
        }
        
        .footer-social a:hover {
            background-color: var(--primary);
        }
        
        .footer-bottom {
            text-align: center;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .footer-bottom p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
        }
        
        /* Responsive Styles */
        @media (max-width: 992px) {
            .about-content, .tech-content-inner {
                flex-direction: column;
                gap: 30px;
            }
            
            .features-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .contact-container {
                flex-direction: column;
            }
        }
        
        @media (max-width: 768px) {
            .menu-toggle {
                display: block;
            }
            
            .nav-links {
                position: fixed;
                top: 80px;
                right: -100%;
                width: 80%;
                height: calc(100vh - 80px);
                background-color: white;
                flex-direction: column;
                align-items: center;
                padding: 40px 0;
                transition: right 0.3s;
                box-shadow: -5px 0 15px rgba(0, 0, 0, 0.1);
            }
            
            .nav-links.active {
                right: 0;
            }
            
            .nav-links li {
                margin: 0 0 20px 0;
            }
            
            .hero h1 {
                font-size: 2.2rem;
            }
            
            .hero p {
                font-size: 1rem;
            }
            
            .hero-buttons {
                flex-direction: column;
                gap: 15px;
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
            
            .section-title h2 {
                font-size: 2rem;
            }
        }
        
        /* Animation */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .animated {
            animation: fadeInUp 0.6s ease-out;
        }
        
        /* Dashboard Animation */
        .dashboard-animation {
            position: relative;
            height: 400px;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            background-color: #1a2233;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
        }
        
        .emotion-dot {
            position: absolute;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: var(--success);
        }
        
        .emotion-dot.happy {
            background-color: var(--success);
        }
        
        .emotion-dot.neutral {
            background-color: var(--info);
        }
        
        .emotion-dot.angry {
            background-color: var(--danger);
        }
        
        .emotion-dot.excited {
            background-color: var(--warning);
        }
        
        .dashboard-stats {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            display: flex;
            justify-content: space-between;
            color: white;
        }
        
        .stat-item {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            flex: 1;
            margin: 0 10px;
        }
        
        .stat-item h4 {
            font-size: 0.9rem;
            margin-bottom: 5px;
            opacity: 0.8;
        }
        
        .stat-item p {
            font-size: 1.5rem;
            font-weight: 700;
        }
        
        .stat-item.happy p {
            color: var(--success);
        }
        
        .stat-item.angry p {
            color: var(--danger);
        }
        
        .stat-item.excited p {
            color: var(--warning);
        }
        
        .stat-item.neutral p {
            color: var(--info);
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container">
            <nav class="navbar">
                <a href="#" class="logo">
                    <i class="fas fa-smile-beam"></i>
                    Emote
                </a>
                <div class="menu-toggle" id="menuToggle">
                    <i class="fas fa-bars"></i>
                </div>
                <ul class="nav-links" id="navLinks">
                    <li><a href="#about">عن المشروع</a></li>
                    <li><a href="#features">المميزات</a></li>
                    <li><a href="#technology">التقنيات</a></li>
                    <li><a href="#dashboard">لوحة التحكم</a></li>
                    <li><a href="#team">فريق العمل</a></li>
                    <li><a href="#contact">تواصل معنا</a></li>
                </ul>
                <a href="#contact" class="cta-button">طلب عرض توضيحي</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content animated">
                <h1>تحليل مشاعر الحشود في الوقت الفعلي</h1>
                <p>نظام Emote المبتكر يستخدم الذكاء الاصطناعي وإنترنت الأشياء لتحليل مشاعر الجماهير وتحسين تجربة المشجعين وضمان سلامتهم في الفعاليات الكبرى</p>
                <div class="hero-buttons">
                    <a href="#about" class="cta-button">تعرف على المزيد</a>
                    <a href="#contact" class="secondary-button">تواصل معنا</a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <div class="section-title animated">
                <h2>عن مشروع Emote</h2>
                <p>نظام مبتكر يهدف إلى تحسين تجربة المشجعين وضمان سلامتهم في الفعاليات الكبرى</p>
            </div>
            <div class="about-content animated">
                <div class="about-image">
                    <img src="https://via.placeholder.com/600x400" alt="Emote System" class="about-image-main">
                </div>
                <div class="about-text">
                    <h3>تحليل المشاعر للحشود في الوقت الفعلي</h3>
                    <p>يعتمد نظام Emote على تقنيات الذكاء الاصطناعي وإنترنت الأشياء (IoT) لتحليل مشاعر الحشود في الوقت الفعلي من خلال تحليل تعابير الوجه ونبرة الصوت وفهم مشاعر الجمهور.</p>
                    <p>يوفر النظام رؤى فورية عن حالة الحشود ويساعد في اتخاذ قرارات مستنيرة لتحسين تجربة المشجعين وضمان سلامتهم.</p>
                    <ul class="feature-list">
                        <li><i class="fas fa-check-circle"></i> تحسين التفاعل الشخصي مع المشجعين</li>
                        <li><i class="fas fa-check-circle"></i> الكشف عن الحالات الطارئة (مثل التوتر أو الغضب) واتخاذ إجراءات سريعة</li>
                        <li><i class="fas fa-check-circle"></i> دعم المنظمين بقرارات مستنيرة لتحسين إدارة الحشود وزيادة الإيرادات</li>
                        <li><i class="fas fa-check-circle"></i> تحليل البيانات لفهم احتياجات الجمهور وتحسين الخدمات المقدمة</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features">
        <div class="container">
            <div class="section-title animated">
                <h2>مميزات النظام</h2>
                <p>يقدم نظام Emote مجموعة من المميزات المتقدمة التي تساعد في تحسين تجربة المشجعين وضمان سلامتهم</p>
            </div>
            <div class="features-grid animated">
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-smile"></i>
                    </div>
                    <h3>تحليل تعابير الوجه</h3>
                    <p>تحليل تعابير الوجه لتحديد مشاعر الحشود (فرح، توتر، غضب) باستخدام كاميرات ذكية وخوارزميات متقدمة للذكاء الاصطناعي.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-volume-up"></i>
                    </div>
                    <h3>تحليل نبرة الصوت</h3>
                    <p>تحليل نبرة الصوت لتحديد مستوى الحماس أو التوتر لدى الجمهور باستخدام ميكروفونات ذكية وتقنيات معالجة الصوت.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h3>تحليل البيانات في الوقت الفعلي</h3>
                    <p>تقديم بيانات في الوقت الفعلي للمنظمين لاتخاذ قرارات فورية تساعد في تحسين تجربة المشجعين وضمان سلامتهم.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-exclamation-triangle"></i>
                    </div>
                    <h3>الكشف عن الحالات الطارئة</h3>
                    <p>الكشف المبكر عن حالات التوتر أو الغضب التي قد تؤدي إلى مواقف غير آمنة واتخاذ إجراءات سريعة لمنع تصاعدها.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-vr-cardboard"></i>
                    </div>
                    <h3>تجارب تفاعلية</h3>
                    <p>تقديم تجارب تفاعلية وشخصية للمشجعين باستخدام تقنيات الواقع المعزز (AR) والواقع الافتراضي (VR).</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-comments"></i>
                    </div>
                    <h3>تحليل التعليقات</h3>
                    <p>تحليل تعليقات المشجعين على وسائل التواصل الاجتماعي لفهم توجهاتهم واحتياجاتهم وتحسين الخدمات المقدمة.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Technology Section -->
    <section id="technology" class="technology">
        <div class="container">
            <div class="section-title animated">
                <h2>التقنيات المستخدمة</h2>
                <p>يعتمد نظام Emote على مجموعة من التقنيات المتقدمة لتحليل مشاعر الحشود في الوقت الفعلي</p>
            </div>
            <div class="tech-tabs animated">
                <button class="tech-tab active" data-tab="ai">الذكاء الاصطناعي</button>
                <button class="tech-tab" data-tab="iot">إنترنت الأشياء</button>
                <button class="tech-tab" data-tab="vr">الواقع المعزز/الافتراضي</button>
                <button class="tech-tab" data-tab="dashboard">لوحة التحكم المركزية</button>
            </div>
            <div class="tech-content active" id="ai-content">
                <div class="tech-content-inner">
                    <div class="tech-image">
                        <img src="https://via.placeholder.com/600x400" alt="AI Technology">
                    </div>
                    <div class="tech-details">
                        <h3>أنظمة الذكاء الاصطناعي</h3>
                        <p>يستخدم نظام Emote أحدث تقنيات الذكاء الاصطناعي لتحليل البيانات الناتجة عن تعابير الوجه ونبرة الصوت وفهم مشاعر الجمهور في الوقت الفعلي.</p>
                        <ul class="tech-list">
                            <li><i class="fas fa-check"></i> خوارزميات متقدمة للتعرف على تعابير الوجه</li>
                            <li><i class="fas fa-check"></i> تقنيات معالجة اللغة الطبيعية لتحليل التعليقات</li>
                            <li><i class="fas fa-check"></i> تحليل نبرة الصوت لتحديد مستوى الحماس أو التوتر</li>
                            <li><i class="fas fa-check"></i> تعلم آلي لتحسين دقة التحليل مع مرور الوقت</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="tech-content" id="iot-content">
                <div class="tech-content-inner">
                    <div class="tech-image">
                        <img src="https://via.placeholder.com/600x400" alt="IoT Technology">
                    </div>
                    <div class="tech-details">
                        <h3>تقنيات إنترنت الأشياء</h3>
                        <p>يعتمد نظام Emote على شبكة من أجهزة الاستشعار والكاميرات الذكية المتصلة لجمع البيانات من البيئة المحيطة وتحليلها في الوقت الفعلي.</p>
                        <ul class="tech-list">
                            <li><i class="fas fa-check"></i> كاميرات ذكية لتحليل تعابير الوجه</li>
                            <li><i class="fas fa-check"></i> ميكروفونات ذكية لتحليل نبرة الصوت</li>
                            <li><i class="fas fa-check"></i> أجهزة استشعار لجمع بيانات بيئية مثل درجة الحرارة ومستوى الضوضاء</li>
                            <li><i class="fas fa-check"></i> شبكة اتصال قوية (مثل 5G) لنقل البيانات بسرعة عالية</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="tech-content" id="vr-content">
                <div class="tech-content-inner">
                    <div class="tech-image">
                        <img src="https://via.placeholder.com/600x400" alt="VR/AR Technology">
                    </div>
                    <div class="tech-details">
                        <h3>تقنيات الواقع المعزز والافتراضي</h3>
                        <p>يستخدم نظام Emote تقنيات الواقع المعزز (AR) والواقع الافتراضي (VR) لتوفير تجارب تفاعلية للمشجعين وتحسين تجربتهم في الفعاليات الكبرى.</p>
                        <ul class="tech-list">
                            <li><i class="fas fa-check"></i> تطبيقات الواقع المعزز لتوفير معلومات إضافية للمشجعين</li>
                            <li><i class="fas fa-check"></i> تجارب الواقع الافتراضي للمشجعين البعيدين عن موقع الحدث</li>
                            <li><i class="fas fa-check"></i> تفاعل مباشر مع البيانات والإحصائيات في الوقت الفعلي</li>
                            <li><i class="fas fa-check"></i> تجارب تفاعلية مخصصة بناءً على تفضيلات المشجعين</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="tech-content" id="dashboard-content">
                <div class="tech-content-inner">
                    <div class="tech-image">
                        <img src="https://via.placeholder.com/600x400" alt="Dashboard Technology">
                    </div>
                    <div class="tech-details">
                        <h3>لوحة التحكم المركزية</h3>
                        <p>توفر لوحة التحكم المركزية في نظام Emote عرضًا شاملاً للبيانات في الوقت الفعلي، مما يساعد المنظمين على اتخاذ قرارات مستنيرة لتحسين تجربة المشجعين وضمان سلامتهم.</p>
                        <ul class="tech-list">
                            <li><i class="fas fa-check"></i> عرض البيانات في الوقت الفعلي بطريقة سهلة الفهم</li>
                            <li><i class="fas fa-check"></i> تنبيهات فورية للحالات الطارئة التي تتطلب تدخلاً سريعًا</li>
                            <li><i class="fas fa-check"></i> تحليلات متقدمة لفهم اتجاهات وسلوكيات المشجعين</li>
                            <li><i class="fas fa-check"></i> واجهة سهلة الاستخدام تتيح للمنظمين اتخاذ إجراءات سريعة</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Dashboard Preview Section -->
    <section id="dashboard" class="dashboard-preview">
        <div class="container">
            <div class="section-title animated">
                <h2>لوحة التحكم المركزية</h2>
                <p>توفر لوحة التحكم المركزية في نظام Emote عرضًا شاملاً للبيانات في الوقت الفعلي</p>
            </div>
            <div class="dashboard-animation animated" id="dashboardAnimation">
                <!-- Emotion dots will be added dynamically with JavaScript -->
                <div class="dashboard-stats">
                    <div class="stat-item happy">
                        <h4>سعيد</h4>
                        <p>68%</p>
                    </div>
                    <div class="stat-item excited">
                        <h4>متحمس</h4>
                        <p>22%</p>
                    </div>
                    <div class="stat-item neutral">
                        <h4>محايد</h4>
                        <p>8%</p>
                    </div>
                    <div class="stat-item angry">
                        <h4>غاضب</h4>
                        <p>2%</p>
                    </div>
                </div>
            </div>
            <div class="dashboard-features animated">
                <div class="dashboard-feature">
                    <i class="fas fa-chart-pie"></i>
                    <h3>تحليل المشاعر</h3>
                    <p>عرض توزيع المشاعر بين الجمهور في الوقت الفعلي لفهم الحالة العامة للحشود.</p>
                </div>
                <div class="dashboard-feature">
                    <i class="fas fa-map-marked-alt"></i>
                    <h3>خريطة حرارية</h3>
                    <p>عرض خريطة حرارية للمكان توضح توزيع المشاعر المختلفة في مناطق مختلفة.</p>
                </div>
                <div class="dashboard-feature">
                    <i class="fas fa-bell"></i>
                    <h3>تنبيهات فورية</h3>
                    <p>إرسال تنبيهات فورية للمنظمين في حالة اكتشاف مستويات عالية من التوتر أو الغضب.</p>
                </div>
                <div class="dashboard-feature">
                    <i class="fas fa-history"></i>
                    <h3>تحليل تاريخي</h3>
                    <p>عرض تحليل تاريخي للمشاعر لفهم الاتجاهات والأنماط على مدار الوقت.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Team Section -->
    <section id="team" class="team">
        <div class="container">
            <div class="section-title animated">
                <h2>فريق العمل</h2>
                <p>فريق متخصص من المبدعين والمطورين وراء تطوير نظام Emote</p>
            </div>
            <div class="team-members animated">
                <div class="team-member">
                    <div class="member-image">
                        <img src="https://via.placeholder.com/300x300" alt="دلال فيحان العصيمي">
                    </div>
                    <div class="member-info">
                        <h3>دلال فيحان العصيمي</h3>
                        <p>مؤسس مشارك ومطور</p>
                        <div class="social-links">
                            <a href="#"><i class="fab fa-twitter"></i></a>
                            <a href="#"><i class="fab fa-linkedin-in"></i></a>
                            <a href="#"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                </div>
                <div class="team-member">
                    <div class="member-image">
                        <img src="https://via.placeholder.com/300x300" alt="سلطان فيحان العصيمي">
                    </div>
                    <div class="member-info">
                        <h3>سلطان فيحان العصيمي</h3>
                        <p>مؤسس مشارك ومطور</p>
                        <div class="social-links">
                            <a href="#"><i class="fab fa-twitter"></i></a>
                            <a href="#"><i class="fab fa-linkedin-in"></i></a>
                            <a href="#"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <div class="section-title animated">
                <h2>تواصل معنا</h2>
                <p>نحن هنا للإجابة على استفساراتك وتقديم المزيد من المعلومات حول نظام Emote</p>
            </div>
            <div class="contact-container animated">
                <div class="contact-info">
                    <h3>معلومات التواصل</h3>
                    <ul class="contact-details">
                        <li>
                            <i class="fas fa-map-marker-alt"></i>
                            <div>
                                <strong>العنوان:</strong>
                                <p>المملكة العربية السعودية، الرياض</p>
                            </div>
                        </li>
                        <li>
                            <i class="fas fa-phone-alt"></i>
                            <div>
                                <strong>الهاتف:</strong>
                                <p>+966 12 345 6789</p>
                            </div>
                        </li>
                        <li>
                            <i class="fas fa-envelope"></i>
                            <div>
                                <strong>البريد الإلكتروني:</strong>
                                <p>info@emote-ai.com</p>
                            </div>
                        </li>
                        <li>
                            <i class="fas fa-clock"></i>
                            <div>
                                <strong>ساعات العمل:</strong>
                                <p>الأحد - الخميس: 9:00 صباحًا - 5:00 مساءً</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <form class="contact-form">
                    <div class="form-group">
                        <label for="name">الاسم</label>
                        <input type="text" id="name" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label for="email">البريد الإلكتروني</label>
                        <input type="email" id="email" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label for="subject">الموضوع</label>
                        <input type="text" id="subject" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label for="message">الرسالة</label>
                        <textarea id="message" class="form-control" required></textarea>
                    </div>
                    <button type="submit" class="submit-btn">إرسال الرسالة</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h3>Emote</h3>
                    <p>نظام مبتكر يهدف إلى تحسين تجربة المشجعين وضمان سلامتهم في الفعاليات الكبرى باستخدام الذكاء الاصطناعي وإنترنت الأشياء.</p>
                    <div class="footer-social">
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                <div class="footer-column">
                    <h3>روابط سريعة</h3>
                    <ul class="footer-links">
                        <li><a href="#about">عن المشروع</a></li>
                        <li><a href="#features">المميزات</a></li>
                        <li><a href="#technology">التقنيات</a></li>
                        <li><a href="#dashboard">لوحة التحكم</a></li>
                        <li><a href="#team">فريق العمل</a></li>
                        <li><a href="#contact">تواصل معنا</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>خدماتنا</h3>
                    <ul class="footer-links">
                        <li><a href="#">تحليل المشاعر</a></li>
                        <li><a href="#">إدارة الحشود</a></li>
                        <li><a href="#">تحسين تجربة المشجعين</a></li>
                        <li><a href="#">تعزيز السلامة</a></li>
                        <li><a href="#">تحليل البيانات</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>النشرة الإخبارية</h3>
                    <p>اشترك في نشرتنا الإخبارية للحصول على آخر التحديثات والأخبار حول نظام Emote.</p>
                    <form class="newsletter-form">
                        <input type="email" placeholder="البريد الإلكتروني" class="form-control">
                        <button type="submit" class="submit-btn">اشتراك</button>
                    </form>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2023 Emote. جميع الحقوق محفوظة.</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile Menu Toggle
        document.getElementById('menuToggle').addEventListener('click', function() {
            document.getElementById('navLinks').classList.toggle('active');
        });
        
        // Smooth Scrolling for Anchor Links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                document.getElementById('navLinks').classList.remove('active');
            });
        });
        
        // Technology Tabs
        const techTabs = document.querySelectorAll('.tech-tab');
        techTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Remove active class from all tabs
                techTabs.forEach(t => t.classList.remove('active'));
                
                // Add active class to clicked tab
                tab.classList.add('active');
                
                // Hide all content
                document.querySelectorAll('.tech-content').forEach(content => {
                    content.classList.remove('active');
                });
                
                // Show corresponding content
                const tabId = tab.getAttribute('data-tab');
                document.getElementById(`${tabId}-content`).classList.add('active');
            });
        });
        
        // Dashboard Animation
        const dashboardAnimation = document.getElementById('dashboardAnimation');
        const emotionTypes = ['happy', 'neutral', 'angry', 'excited'];
        
        // Create initial dots
        for (let i = 0; i < 100; i++) {
            createEmotionDot();
        }
        
        // Continue creating dots at intervals
        setInterval(createEmotionDot, 300);
        
        function createEmotionDot() {
            const dot = document.createElement('div');
            dot.classList.add('emotion-dot');
            
            // Assign random emotion type with weighted probability
            const rand = Math.random();
            if (rand < 0.68) {
                dot.classList.add('happy');
            } else if (rand < 0.9) {
                dot.classList.add('excited');
            } else if (rand < 0.98) {
                dot.classList.add('neutral');
            } else {
                dot.classList.add('angry');
            }
            
            // Random position
            const x = Math.floor(Math.random() * dashboardAnimation.offsetWidth);
            const y = Math.floor(Math.random() * (dashboardAnimation.offsetHeight - 100));
            
            dot.style.left = x + 'px';
            dot.style.top = y + 'px';
            
            dashboardAnimation.appendChild(dot);
            
            // Remove dot after animation
            setTimeout(() => {
                dot.remove();
            }, 5000);
        }
        
        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                }
            });
        }, observerOptions);
        
        document.querySelectorAll('.section-title, .about-content, .features-grid, .tech-tabs, .dashboard-animation, .dashboard-features, .team-members, .contact-container').forEach(el => {
            el.classList.remove('animated');
            observer.observe(el);
        });
    </script>
</body>
</html>
