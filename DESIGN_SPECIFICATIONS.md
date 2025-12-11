# Design Specifications - DeepFake Detection App

## 🎯 Design Goals
- Modern, attractive, professional appearance
- Clear visual hierarchy and user guidance
- Consistent theme throughout all pages
- Responsive design for all devices
- Enhanced user engagement with animations

---

## 🎨 Visual Design System

### Primary Colors
```css
/* Primary Gradient (Used throughout) */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Semantic Colors */
--success: #28a745;    /* Real/Authentic */
--danger: #dc3545;     /* Fake/Deepfake */
--warning: #ffc107;    /* Demo Mode */
--info: #0d6efd;       /* Information */
```

### Secondary Gradient Palettes
```css
/* Pink Gradient */
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);

/* Cyan Gradient */
background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);

/* Green Gradient */
background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);

/* Success Gradient */
background: linear-gradient(135deg, #28a745 0%, #20c997 100%);

/* Danger Gradient */
background: linear-gradient(135deg, #dc3545 0%, #e74c3c 100%);
```

---

## 🔤 Typography

### Font Stack
```css
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
```

### Font Sizes & Weights
| Element | Size | Weight | Usage |
|---------|------|--------|-------|
| Display 1 | 4em | 700 | Major titles |
| Display 3 | 2.5em | 700 | Page headings |
| h1 | 2.5em | 700 | Section titles |
| h2 | 2em | 700 | Subsection titles |
| h3 | 1.5em | 700 | Card titles |
| h4 | 1.3em | 700 | Minor titles |
| h5 | 1.1em | 700 | Labels |
| Lead | 1.3em | 400 | Descriptions |
| Body | 1em | 400 | Regular text |
| Small | 0.95em | 400 | Supplementary text |

---

## 🎭 Component Specifications

### Buttons
```css
.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 20px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}
```

### Cards
```css
.card {
  border: none;
  border-radius: 24px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  overflow: hidden;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.2);
}
```

### Result Badges
```css
/* REAL Result */
.badge-real {
  background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
  color: white;
  padding: 40px;
  border-radius: 24px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}

/* DEEPFAKE Result */
.badge-fake {
  background: linear-gradient(135deg, #dc3545 0%, #e74c3c 100%);
  color: white;
  padding: 40px;
  border-radius: 24px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}
```

### Progress Bars
```css
.progress {
  height: 45px;
  border-radius: 20px;
  background: #e9ecef;
  overflow: hidden;
}

.progress-bar {
  font-size: 1.1em;
  font-weight: bold;
  line-height: 45px;
  transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Form Inputs
```css
.form-control {
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 12px 16px;
  transition: all 0.3s ease;
}

.form-control:focus {
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}
```

---

## 🎬 Animations & Transitions

### Hover Effects
```css
/* Lift Effect */
.hover-lift:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
}

/* Scale Effect */
.hover-scale:hover {
  transform: scale(1.05);
}

/* Slide Effect */
.hover-slide:hover {
  transform: translateX(3px);
}
```

### Transition Timings
```css
/* Standard Transition */
transition: all 0.3s ease;

/* Progress Bar */
transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);

/* Slow Transition */
transition: all 0.5s ease-out;
```

### Keyframe Animations
```css
@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

## 🧊 Spacing System

### Padding Scale
- `p-1`: 0.25rem
- `p-2`: 0.5rem
- `p-3`: 1rem
- `p-4`: 1.5rem
- `p-5`: 3rem

### Margin Scale
- `m-1`: 0.25rem
- `m-2`: 0.5rem
- `m-3`: 1rem
- `m-4`: 1.5rem
- `m-5`: 3rem

### Border Radius
- `rounded`: 0.25rem
- `rounded-1`: 0.25rem
- `rounded-2`: 0.5rem
- `rounded-3`: 0.75rem
- `rounded-4`: 1.5rem
- `rounded-5`: 2rem
- `rounded-circle`: 50%

---

## 🌐 Responsive Breakpoints

### Bootstrap Grid Breakpoints
```css
/* Small devices (landscape phones, 576px and up) */
@media (min-width: 576px) { ... }

/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) { ... }

/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) { ... }

/* Extra large devices (large desktops, 1200px and up) */
@media (min-width: 1200px) { ... }
```

### Column Classes
- `.col-12`: Full width on mobile
- `.col-md-6`: 50% width on tablet
- `.col-lg-4`: 33.33% width on desktop
- `.col-lg-6`: 50% width on desktop

---

## 🔍 Shadow System

```css
/* Light Shadow */
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

/* Medium Shadow */
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);

/* Large Shadow */
box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);

/* Extra Large Shadow */
box-shadow: 0 15px 50px rgba(0, 0, 0, 0.2);

/* Gradient Shadow */
box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
```

---

## 🎯 Navigation Bar Specifications

### Colors
- Background: Purple gradient
- Text: White
- Hover State: Slightly lighter white with translateY(-2px)

### Structure
```
[Logo + Brand] ---- [Home] [About] [GitHub]
```

### Heights & Spacing
- Height: Auto (content-driven)
- Padding: 1rem on top/bottom
- Icon spacing: 0.5rem between icon and text

---

## 📱 Mobile Design Patterns

### Stack Elements On Mobile
```css
@media (max-width: 767px) {
  .row > .col-md-6 {
    width: 100%;
  }
  
  .row > .col-lg-4 {
    width: 100%;
  }
}
```

### Text Sizing
- Reduce font sizes by 10-15% on mobile
- Increase line-height for readability
- Maintain good contrast ratios (WCAG AA)

### Touch Targets
- Minimum 44x44px for interactive elements
- Adequate spacing between clickable items (8-16px)

---

## 🎨 Icon Usage

### Font Awesome 6.4.0 Classes
- Icons: `<i class="fas fa-{icon-name}"></i>`
- Common Icons:
  - Shield: `fas fa-shield-alt`
  - Video: `fas fa-video`
  - Home: `fas fa-home`
  - Info: `fas fa-info-circle`
  - GitHub: `fab fa-github`
  - Check: `fas fa-check-circle`
  - Warning: `fas fa-exclamation-triangle`

### Icon Sizing
```css
.fa-sm { font-size: 0.875em; }
.fa-1x { font-size: 1em; }
.fa-2x { font-size: 2em; }
.fa-3x { font-size: 3em; }
```

---

## 🔄 Consistency Guidelines

### Color Usage
- Gradients should always be at 135deg
- Primary actions use main gradient
- Success/Danger actions use semantic colors
- Backgrounds should provide sufficient contrast

### Spacing
- Consistent padding within cards (24-40px)
- Consistent margins between sections (2-3rem)
- Consistent padding in buttons (12-16px)

### Typography
- Use bold for headings and important text
- Use regular for body and descriptions
- Maintain size hierarchy consistently

### Shadows
- Light shadows for subtle elevation
- Medium shadows for cards
- Large shadows for modals and overlays

---

## ✨ Brand Elements

### Logo/Brand Text
- Icon: Shield from Font Awesome
- Text: "DeepFake Detector"
- Color: White on gradient background
- Font Weight: Bold (700)

### Tagline
"Advanced AI technology to detect and identify artificially manipulated video content"

### Call-to-Action
- Primary: "Analyze Video" / "Start Analyzing"
- Secondary: "Upload Video" / "Choose File"
- Tertiary: "Learn More" / "Analyze Another Video"

---

## 🚀 Performance Considerations

### Image Optimization
- Use WebP format where supported
- Lazy load images below the fold
- Optimize video thumbnails

### CSS Optimization
- Use CSS Grid/Flexbox for layouts
- Minimize box-shadow usage on mobile
- Hardware-accelerate animations with `transform`

### Animation Performance
- Use `transform` and `opacity` for animations
- Avoid animating `top`, `left`, `width`, `height`
- Keep animation duration to 0.3-0.8 seconds

---

## 📋 Accessibility

### Color Contrast
- Minimum 4.5:1 for text on backgrounds
- Ensure text is readable on gradient backgrounds
- Use both color and icons for status indication

### Keyboard Navigation
- All interactive elements focusable
- Visible focus indicators
- Tab order should be logical

### Alt Text
- Provide alt text for all images
- Use aria-labels for icon buttons
- Describe video content

---

**Last Updated**: December 11, 2025
**Design Version**: 2.0
**Framework**: Bootstrap 4.4.1 + Custom CSS
