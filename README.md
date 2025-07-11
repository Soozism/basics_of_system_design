# System Design Tutorial Website

A comprehensive HTML website for learning system design concepts, converted from Markdown files.

🌐 **Live Website:** [https://soozism.github.io/basics_of_system_design/](https://soozism.github.io/basics_of_system_design/)

## Features

- 📚 **67 Pages** of system design content
- 🎨 **Modern Design** with responsive layout
- 🔍 **Easy Navigation** with sidebar and breadcrumbs
- 📱 **Mobile-Friendly** design
- 🎯 **Persian/Farsi** language support
- 🔗 **Cross-referenced** content with internal links
- 🚀 **GitHub Pages** deployment from development branch

## Structure

```
html_website/
├── index.html                 # Main homepage
├── sitemap.html              # Complete page listing
├── css/
│   └── style.css             # Main stylesheet
├── js/
│   └── script.js             # Interactive features
├── convert_md_to_html.py     # Conversion script
└── [Content Pages]/          # All converted HTML pages
    ├── Basic concepts of system design/
    ├── Main components of scalable systems/
    ├── Designing scalable and reliable systems/
    ├── Advanced Topics in System Design/
    └── Preparing for System Design Interviews/
```

## How to Use

1. **Open the Website**
   - Open `index.html` in your web browser
   - Or start with `sitemap.html` to see all available pages

2. **Navigate the Content**
   - Use the main navigation menu at the top
   - Use the sidebar for section-specific navigation
   - Follow the breadcrumb trail to track your location

3. **Study Path**
   - Start with "Basic Concepts" for fundamentals
   - Progress through "Main Components" for building blocks
   - Learn "Scalable Systems" for practical applications
   - Explore "Advanced Topics" for deeper understanding
   - Practice with "Interview Questions" for preparation

## Content Sections

### 1. Basic Concepts (مفاهیم پایه‌ای)
- Introduction to System Design
- Software Architecture Components
- Key Concepts in System Design

### 2. Main Components (اجزای اصلی)
- Databases and Storage
- Caching
- Microservices Architecture
- Messaging and Queues

### 3. Scalable Systems (سیستم‌های مقیاس‌پذیر)
- Load Balancing
- Horizontal and Vertical Scalability
- Failure Management and Fault Tolerance

### 4. Advanced Topics (موضوعات پیشرفته)
- Distributed Systems
- Big Data Processing
- Security in System Design
- Monitoring and Observability

### 5. Interview Preparation (آمادگی مصاحبه)
- Problem-Solving Approach
- Sample Interview Questions

## Technical Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern CSS**: Uses CSS Grid and Flexbox for layout
- **Interactive JavaScript**: Smooth scrolling, mobile menu, search
- **Print-Friendly**: Optimized for printing
- **Accessibility**: Proper heading structure and keyboard navigation

## Browser Support

- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+

## File Organization

All original Markdown files have been converted to HTML while maintaining the same directory structure. Each HTML file includes:

- Proper page title and metadata
- Responsive navigation
- Breadcrumb navigation
- Styled content with proper typography
- Links to related topics

## Customization

### Colors
The website uses CSS custom properties (variables) for easy theming:
- `--primary-color`: Main brand color
- `--secondary-color`: Secondary brand color
- `--accent-color`: Accent color for highlights
- `--text-primary`: Main text color
- `--text-secondary`: Secondary text color

### Fonts
The website uses system fonts for better performance:
- Primary: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto
- Code: 'Consolas', 'Monaco', 'Courier New', monospace

## Performance

- Lightweight CSS and JavaScript
- Optimized images (when added)
- Minimal external dependencies
- Fast loading times

## Contributing

To add new content:
1. Create new Markdown files in appropriate directories
2. Run the conversion script: `python convert_md_to_html.py`
3. Update navigation links if needed

## License

This educational content is provided for learning purposes.

## Deployment

This website is automatically deployed to GitHub Pages using GitHub Actions.

### Deployment Process
- The site is deployed from the `development` branch
- GitHub Actions workflow (`.github/workflows/deploy.yml`) handles automatic deployment
- Any push to the `development` branch triggers a new deployment
- The live site is available at: https://soozism.github.io/basics_of_system_design/

### Local Development
To run the site locally:
```bash
# Using Python's built-in server
python serve.py

# Or using the batch file (Windows)
start_server.bat
```

The site will be available at `http://localhost:8000`

---

**Last Updated**: December 2024
**Total Pages**: 67
**Languages**: Persian/Farsi
**Status**: Complete conversion from Markdown to HTML
