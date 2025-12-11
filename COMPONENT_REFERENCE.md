# 🎨 UI Components & Code Examples

## Quick Reference Guide for Developers

---

## 📦 Reusable Components

### 1. Primary Gradient Button
```html
<a href="#" class="btn btn-lg rounded-3 px-5" 
   style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
          color: white; 
          border: none;">
  <i class="fas fa-icon me-2"></i>Button Text
</a>
```

**CSS for Styling:**
```css
.btn-primary-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 20px;
  padding: 12px 24px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-primary-gradient:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}
```

---

### 2. Feature Card (with Gradient Border)
```html
<div class="rounded-4 overflow-hidden shadow-lg" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3px;">
  <div style="background: white; padding: 40px; border-radius: 15px;">
    <h5 class="fw-bold mb-3" style="color: #333;">
      <i class="fas fa-icon me-2" style="color: #667eea;"></i>Card Title
    </h5>
    <p style="color: #555; line-height: 1.8;">
      Card content goes here...
    </p>
  </div>
</div>
```

---

### 3. Result Badge (REAL)
```html
<div class="result-badge rounded-4 p-5" 
     style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); 
             color: white;
             box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);">
  <div class="display-1 fw-bold mb-3" style="line-height: 1;">✓</div>
  <h2 class="h1 fw-bold mb-3">REAL VIDEO</h2>
  <p class="lead mb-0">This video appears to be genuine and not AI-generated</p>
</div>
```

---

### 4. Result Badge (DEEPFAKE)
```html
<div class="result-badge rounded-4 p-5" 
     style="background: linear-gradient(135deg, #dc3545 0%, #e74c3c 100%); 
             color: white;
             box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);">
  <div class="display-1 fw-bold mb-3" style="line-height: 1;">⚠</div>
  <h2 class="h1 fw-bold mb-3">DEEPFAKE DETECTED</h2>
  <p class="lead mb-0">This video appears to be AI-generated or artificially manipulated</p>
</div>
```

---

### 5. Confidence Progress Bar
```html
<div class="progress rounded-3" style="height: 45px; background: #e9ecef;">
  <div class="progress-bar {% if output == 'REAL' %}bg-success{% else %}bg-danger{% endif %} rounded-3" 
       role="progressbar" 
       style="width: {{confidence}}%; font-size: 1.1em; font-weight: bold; line-height: 45px;" 
       aria-valuenow="{{confidence}}" 
       aria-valuemin="0" 
       aria-valuemax="100">
    {{confidence}}%
  </div>
</div>
```

---

### 6. Info Card with Icon
```html
<div class="card rounded-4 shadow-lg border-0 hover-lift h-100" 
     style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
  <div class="card-body text-center p-4">
    <div class="display-6 mb-3"><i class="fas fa-icon"></i></div>
    <h5 class="card-title fw-bold">Card Title</h5>
    <p class="card-text mb-0" style="font-size: 0.9em;">Card description text</p>
  </div>
</div>
```

---

### 7. Section Header with Icon
```html
<h2 class="h2 fw-bold mb-5" style="color: #333;">
  <i class="fas fa-icon me-3" style="color: #667eea;"></i>Section Title
</h2>
```

---

### 8. Alert Box (Warning)
```html
<div class="alert alert-warning rounded-3 mb-0" style="border: none;">
  <i class="fas fa-lightbulb me-2"></i>
  <strong>Demo Mode:</strong> Using frame analysis algorithm. For production, install ML model for higher accuracy.
</div>
```

---

### 9. Navigation Link with Icon
```html
<li class="nav-item">
  <a class="nav-link text-white fw-bold" href="{% url 'ml_app:home' %}" 
     style="transition: all 0.3s ease;">
    <i class="fas fa-home me-2"></i>Home
  </a>
</li>
```

---

### 10. Hover Lift Card
```html
<div class="card rounded-4 shadow-lg border-0 hover-lift" 
     style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
  <div class="card-body">
    <!-- Content -->
  </div>
</div>

<style>
  .hover-lift:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2) !important;
  }
</style>
```

---

## 🎯 Common Patterns

### 2-Column Layout (Responsive)
```html
<div class="row align-items-center mb-5">
  <div class="col-lg-6 mb-4 mb-lg-0">
    <!-- Left column content -->
  </div>
  <div class="col-lg-6">
    <!-- Right column content -->
  </div>
</div>
```

---

### 3-Column Grid (Cards)
```html
<div class="row g-3">
  <div class="col-md-6 col-lg-4">
    <!-- Card 1 -->
  </div>
  <div class="col-md-6 col-lg-4">
    <!-- Card 2 -->
  </div>
  <div class="col-md-6 col-lg-4">
    <!-- Card 3 -->
  </div>
</div>
```

---

### 4-Column Grid (Stats)
```html
<div class="row">
  <div class="col-md-6 col-lg-3 mb-4">
    <!-- Card -->
  </div>
  <div class="col-md-6 col-lg-3 mb-4">
    <!-- Card -->
  </div>
  <div class="col-md-6 col-lg-3 mb-4">
    <!-- Card -->
  </div>
  <div class="col-md-6 col-lg-3 mb-4">
    <!-- Card -->
  </div>
</div>
```

---

## 🎨 Gradient Combinations

### Primary Gradient
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```
**Use for**: Main buttons, navigation, primary actions

### Pink Gradient
```css
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
```
**Use for**: Secondary actions, accent elements

### Cyan Gradient
```css
background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
```
**Use for**: Info sections, secondary features

### Green Gradient
```css
background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
```
**Use for**: Success elements, positive feedback

### Success Gradient
```css
background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
```
**Use for**: REAL detection results

### Danger Gradient
```css
background: linear-gradient(135deg, #dc3545 0%, #e74c3c 100%);
```
**Use for**: DEEPFAKE detection results

---

## 📐 Spacing Quick Reference

### Padding Classes
- `p-1` = 0.25rem
- `p-2` = 0.5rem
- `p-3` = 1rem (standard)
- `p-4` = 1.5rem (comfortable)
- `p-5` = 3rem (generous)

### Margin Classes
- `m-1` = 0.25rem
- `m-2` = 0.5rem
- `m-3` = 1rem
- `m-4` = 1.5rem
- `m-5` = 3rem

### Gap Classes (Grid)
- `g-1` = 0.25rem
- `g-2` = 0.5rem
- `g-3` = 1rem
- `g-4` = 1.5rem
- `g-5` = 3rem

---

## 🔤 Font Size Hierarchy

### Heading Sizes
- `.display-1` = 5.5rem (largest)
- `.display-3` = 3.5rem
- `.h1` = 2.5rem
- `.h2` = 2rem
- `.h3` = 1.75rem
- `.h4` = 1.5rem
- `.h5` = 1.25rem
- `.h6` = 1rem

### Text Sizes
- `.lead` = 1.3em (introductory)
- `p` (normal) = 1em
- `.small` = 0.9em
- `.text-muted` = smaller, lighter

---

## 🎬 Animation Classes & Styles

### Hover Lift
```css
.hover-lift:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
}
```

### Button Hover
```css
.btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}
```

### Scale Hover
```css
.hover-scale:hover {
  transform: scale(1.05);
}
```

### Slide Hover
```css
.hover-slide:hover {
  transform: translateX(3px);
}
```

### Opacity Hover
```css
a:hover {
  opacity: 1;
}
```

---

## 🌐 Bootstrap Classes Reference

### Display & Layout
- `.d-flex` = display: flex
- `.justify-content-center` = justify-content: center
- `.align-items-center` = align-items: center
- `.text-center` = text-align: center
- `.text-white` = color: white

### Sizing
- `.w-100` = width: 100%
- `.h-100` = height: 100%
- `.min-h-100` = min-height: 100%

### Borders & Shadows
- `.rounded` = border-radius: 0.25rem
- `.rounded-4` = border-radius: 1.5rem
- `.border-0` = border: none
- `.shadow` = box-shadow (light)
- `.shadow-lg` = box-shadow (large)

### Typography
- `.fw-bold` = font-weight: 700
- `.text-muted` = lighter text color
- `.text-white` = white text
- `.text-center` = center text

### Spacing
- `.mb-4` = margin-bottom: 1.5rem
- `.mt-5` = margin-top: 3rem
- `.px-5` = padding-left & right: 3rem
- `.ps-md-4` = padding-left on medium screens

---

## 🎯 Font Awesome Icons

### Common Icons Used
```html
<i class="fas fa-shield-alt"></i>     <!-- Shield -->
<i class="fas fa-home"></i>            <!-- Home -->
<i class="fas fa-video"></i>           <!-- Video -->
<i class="fas fa-info-circle"></i>     <!-- Info -->
<i class="fas fa-check-circle"></i>    <!-- Check -->
<i class="fas fa-exclamation-triangle"></i> <!-- Warning -->
<i class="fab fa-github"></i>          <!-- GitHub -->
<i class="fab fa-linkedin"></i>        <!-- LinkedIn -->
<i class="fab fa-twitter"></i>         <!-- Twitter -->
<i class="fas fa-arrow-left"></i>      <!-- Back arrow -->
<i class="fas fa-chart-pie"></i>       <!-- Statistics -->
<i class="fas fa-brain"></i>           <!-- AI/Brain -->
<i class="fas fa-face-smile"></i>      <!-- Face -->
<i class="fas fa-heart"></i>           <!-- Heart -->
```

---

## 🔄 Responsive Helpers

### Hide on Mobile
```html
<div class="d-none d-md-block">
  <!-- Hidden on small screens, visible on medium+ -->
</div>
```

### Show Only on Mobile
```html
<div class="d-md-none">
  <!-- Visible on small screens, hidden on medium+ -->
</div>
```

### Text Alignment by Screen
```html
<div class="text-center text-md-start">
  <!-- Centered on mobile, left-aligned on tablet+ -->
</div>
```

---

## 📋 Testing Checklist

- [ ] Mobile (320px, 375px, 425px)
- [ ] Tablet (768px, 1024px)
- [ ] Desktop (1200px, 1920px)
- [ ] Hover effects work
- [ ] Colors contrast properly
- [ ] Icons display correctly
- [ ] Forms are usable on touch
- [ ] Navigation is accessible
- [ ] Animations perform smoothly
- [ ] All links are functional

---

## 🚀 Best Practices

### DO
- ✅ Use gradients for visual interest
- ✅ Include icons for visual hierarchy
- ✅ Maintain consistent spacing
- ✅ Use semantic colors (green/red for status)
- ✅ Test on multiple screen sizes
- ✅ Use CSS transforms for animations
- ✅ Include focus states for accessibility
- ✅ Provide feedback for interactions

### DON'T
- ❌ Use too many colors
- ❌ Animate non-transform properties
- ❌ Forget mobile responsiveness
- ❌ Skip accessibility features
- ❌ Use low contrast combinations
- ❌ Add animations that distract
- ❌ Forget alt text for images
- ❌ Use outdated browser features

---

## 📚 Resources

### Documentation Files
- `DESIGN_SPECIFICATIONS.md` - Detailed design system
- `UI_ENHANCEMENTS_SUMMARY.md` - What was changed
- `README_UI_REDESIGN.md` - Complete redesign overview

### External Resources
- Bootstrap 4: https://getbootstrap.com/docs/4.1/
- Font Awesome: https://fontawesome.com/icons/
- CSS Gradients: https://developer.mozilla.org/en-US/docs/Web/CSS/linear-gradient()

---

**Last Updated**: December 11, 2025
**Version**: 2.0
**For**: DeepFake Detection Application
