# 🎨 DeepFake Detection - Visual Reference Card

## Quick Visual Guide

---

## 🌈 Color Palette Reference

### Primary Purple Gradient
```
#667eea (blue) ──→ #764ba2 (purple)
  135° angle
```
**Use**: Buttons, navigation, main CTAs, headers

### Result Colors
```
REAL (Green)
#28a745 → #20c997
SUCCESS

DEEPFAKE (Red)
#dc3545 → #e74c3c
DANGER
```

### Accent Gradients
```
Pink:  #f093fb → #f5576c
Cyan:  #4facfe → #00f2fe
Teal:  #43e97b → #38f9d7
```

---

## 🔤 Typography Scale

```
Display 1    4.0em    LARGEST TITLES
Display 3    3.5em    PAGE HEADINGS
h1           2.5em    ├─ Section Headings
h2           2.0em    │
h3           1.75em   ├─ Subsections
h4           1.5em    │
h5           1.25em   └─ Labels
h6           1.0em    

Lead         1.3em    Introductory Text
Body         1.0em    Regular Content
Small        0.9em    Supplementary
```

---

## 📏 Spacing System

### Padding (Inside elements)
```
p-1    0.25rem  ░░░░░░░░░░░░░░░░░░░░░░░░░░░
p-2    0.5rem   ░░░░░░░░░░░░░░░░░░░░░░░░░░
p-3    1.0rem   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
p-4    1.5rem   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
p-5    3.0rem   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

### Border Radius
```
rounded      4px      □
rounded-1    4px      □
rounded-2    8px      ⬜
rounded-3   12px      ⬜
rounded-4   24px      ⚫   (STANDARD)
rounded-5   32px      ⚫
```

---

## 🎭 Component Visual Guide

### Button Styles

**Primary Gradient Button**
```
┌────────────────────────┐
│ 📹 Analyze Video       │  Purple Gradient
│ Transform: translateY  │  Hover: Lifted
└────────────────────────┘
```

### Card Styles

**Feature Card (with border)**
```
═════════════════════════════════════════
║ ╔─────────────────────────────────────╗║
║ ║  🎯 Card Title                       ║║
║ ║                                       ║║
║ ║  Card content goes here...          ║║
║ ║  Hover: Lifted by 10px              ║║
║ ║                                       ║║
║ ╚─────────────────────────────────────╝║
═════════════════════════════════════════
```

### Result Badge

**REAL Result**
```
╔══════════════════════════╗
║                          ║
║         ✓                ║  Green Gradient
║    REAL VIDEO           ║  Large Icon
║                          ║
╚══════════════════════════╝
```

**DEEPFAKE Result**
```
╔══════════════════════════╗
║                          ║
║         ⚠                ║  Red Gradient
║  DEEPFAKE DETECTED       ║  Warning Icon
║                          ║
╚══════════════════════════╝
```

### Progress Bar

**Confidence Meter**
```
┌──────────────────────────────────┐
│████████████░░░░░░░░░░░░░░ 85%    │  Animated Fill
└──────────────────────────────────┘
```

---

## 📱 Responsive Grid

### Mobile (< 576px)
```
┌──────────┐
│  Col 12  │  Full width on phone
└──────────┘
┌──────────┐
│  Col 12  │
└──────────┘
```

### Tablet (768px - 991px)
```
┌────────┬────────┐
│ Col 6  │ Col 6  │  2 columns on tablet
└────────┴────────┘
```

### Desktop (992px+)
```
┌────┬────┬────┬────┐
│Col4│Col4│Col4│Col4│  4 columns on desktop
└────┴────┴────┴────┘
```

---

## 🎬 Animation Reference

### Hover Effects Timeline

**Card Lift**
```
Default:   ━━━━━━━━━━━
           ┌─────────┐  Initial
           │  Card   │
           └─────────┘

Hover:         ┌─────────┐
               │  Card   │  Lifted 10px
               └─────────┘
               (0.3s ease)
```

**Button Scale**
```
Default:   ┌────┐     Normal
           │Btn │
           └────┘

Hover:        ┌──────┐
              │ Btn  │  Scaled 1.05x
              └──────┘
              (0.3s ease)
```

**Progress Fill**
```
0%:    ░░░░░░░░░░░░░░░░░
85%:   ████████████░░
       (0.8s cubic-bezier)
```

---

## 🎯 Visual Hierarchy

### Importance Levels

**Level 1 - Most Important**
```
████████████████████████  Large bold text
Largest font size        Color: Primary gradient
```

**Level 2 - Important**
```
████████████████         Medium font size
Dark text               Color: Dark gray/blue
```

**Level 3 - Supporting**
```
████████████            Smaller font size
Lighter text           Color: Muted gray
```

**Level 4 - Supplementary**
```
████████                Very small
Very light text        Color: Light gray
```

---

## 🌊 Shadow Depth Levels

### Light Shadow (Subtle)
```
▭▭▭▭▭▭▭▭▭▭▭▭▭▭  0 2px 8px rgba(0,0,0,0.1)
Card slightly elevated
```

### Medium Shadow
```
▔▔▔▔▔▔▔▔▔▔▔▔▔▔  0 4px 15px rgba(0,0,0,0.1)
Card elevated
```

### Large Shadow
```
▔▔▔▔▔▔▔▔▔▔▔▔▔▔  0 10px 40px rgba(0,0,0,0.15)
Card prominently elevated
```

### Extra Large Shadow
```
▔▔▔▔▔▔▔▔▔▔▔▔▔▔  0 15px 50px rgba(0,0,0,0.2)
Modal/overlay depth
```

---

## 🎪 Layout Patterns

### 3-Column Feature Grid
```
┌────────┬────────┬────────┐
│Feature │Feature │Feature │
│  Card  │  Card  │  Card  │
└────────┴────────┴────────┘
(Responsive: 2 col on tablet, 1 col on mobile)
```

### 2-Column with Sidebar
```
┌─────────────────────┬──────────┐
│   Main Content      │ Sidebar  │
│                     │  Info    │
│                     │  Section │
└─────────────────────┴──────────┘
```

### Hero + Grid
```
═════════════════════════════════════
║         LARGE TITLE               ║
║         HERO SECTION              ║
═════════════════════════════════════

┌────────┬────────┬────────┐
│  Card  │  Card  │  Card  │
└────────┴────────┴────────┘
```

---

## 🎨 Gradient Direction Guide

### 135 Degrees (Standard)
```
    ╔════════════╗
    ║ ╱ light    ║  Upper-left to
  ╱ ║ ╱          ║  lower-right
╱   ║╱ dark      ║  (Most common)
    ╚════════════╝
```

### Other Directions
```
Top    │         Right    ──→
to     ↓         to
Bottom             Left    ←──
```

---

## 📊 Icon Sizing Guide

```
Very Small:   0.875em  🎨 Small badge icons
Small:        1em      🎨 Text-level icons  
Medium:       1.5em    🎨 Card titles
Large:        2em      🎨 Section headers
Extra Large:  3em+     🎨 Hero sections
```

---

## ♿ Accessibility Quick Check

### Color Contrast
```
Light text on dark:  4.5:1 ratio ✅
Dark text on light:  4.5:1 ratio ✅
Both gradient colors tested ✅
```

### Focus States
```
Default:   Regular button
Focused:   Blue outline visible
Active:    Darker background
Hover:     Lifted with shadow
```

### Touch Targets
```
Minimum:   44x44px (2.75rem)
Actual:    50x50px + padding
Spacing:   8px minimum between targets
```

---

## 📋 Component Checklist

### Button ✅
- [ ] Gradient background
- [ ] Rounded corners (20px)
- [ ] Font weight: 600
- [ ] Padding: 12px 24px
- [ ] Hover: translate + shadow
- [ ] Icon spacing: 0.5rem

### Card ✅
- [ ] Border radius: 24px
- [ ] Box shadow: large
- [ ] Overflow: hidden
- [ ] Padding: 20-40px
- [ ] Hover: lift effect
- [ ] Responsive width

### Progress Bar ✅
- [ ] Height: 45px
- [ ] Border radius: 20px
- [ ] Font weight: bold
- [ ] Animation: 0.8s cubic
- [ ] Percentage display
- [ ] Color coding

---

## 🚀 Performance Checklist

### CSS
- [x] Use transform for animations
- [x] Use opacity for fades
- [x] GPU acceleration enabled
- [x] No expensive box-shadows on small devices

### Images
- [x] Optimized file sizes
- [x] Appropriate formats
- [x] Lazy loaded

### Fonts
- [x] System fonts preferred
- [x] Font Awesome from CDN
- [x] Minimal font variations

---

## 🎓 Design Principles

### 1. Consistency
Every element follows the same patterns and standards

### 2. Hierarchy
Clear visual importance through size, color, position

### 3. Feedback
User interactions show immediate visual response

### 4. Accessibility
Inclusive design for all users

### 5. Simplicity
Remove unnecessary elements, focus on content

### 6. Responsiveness
Works seamlessly on all device sizes

---

## 🔗 Quick Links

**Colors**: #667eea, #764ba2, #28a745, #dc3545  
**Font**: Segoe UI, Tahoma, Geneva, Verdana  
**Radius**: 24px (rounded-4)  
**Shadow**: 0 10px 40px rgba(0,0,0,0.1)  
**Duration**: 0.3s ease (standard)  

---

**Last Updated**: December 11, 2025  
**Version**: 2.0  
**Reference Type**: Quick Visual Guide
