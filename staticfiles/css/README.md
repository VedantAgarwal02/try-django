# Blog CSS Architecture

A modular, industry-standard CSS system for the Django blogs application with a modern, minimal aesthetic.

## Project Structure

```
static/css/
├── style.css              # Main entry point (imports all modules)
├── variables.css          # Design system tokens (colors, spacing, typography)
├── base.css              # Global styles and resets
├── components.css        # Reusable UI components (nav, cards, buttons, badges)
└── blogs/
    └── articles.css      # Blog-specific styles (article cards, details pages)
```

## Design System

### Color Palette
- **Primary**: `#2c3e50` - Main text and UI elements
- **Secondary**: `#3498db` - Links and accents
- **Accent**: `#e74c3c` - Highlights and CTAs
- **Backgrounds**: `#ffffff` (primary), `#f8f9fa` (secondary), `#ecf0f1` (tertiary)

### Spacing Scale (8px base unit)
All spacing uses CSS variables: `--spacing-xs`, `--spacing-sm`, `--spacing-base`, `--spacing-md`, `--spacing-lg`, `--spacing-xl`, `--spacing-2xl`

### Typography
- **Font Family**: System font stack for maximum compatibility
- **Size Scale**: `--font-size-xs` through `--font-size-4xl`
- **Weights**: Light (300), Normal (400), Semibold (600), Bold (700)
- **Line Heights**: Tight (1.2), Normal (1.5), Relaxed (1.75)

### Border Radius
Consistent rounded corners: `--radius-sm`, `--radius-base`, `--radius-md`, `--radius-lg`, `--radius-xl`

### Shadows
Layered shadows for depth: `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-xl`

### Transitions
Smooth animations at three speeds:
- Fast: 150ms
- Base: 250ms
- Slow: 350ms

## Key Components

### Article Cards (`.article-card`)
- Hover effects with lift animation (`translateY(-8px)`)
- Dynamic title color change on hover
- Responsive grid layout (auto-fill with 300px minimum width)
- Excerpt truncation (3 lines max)
- Meta information with icons

### Article Detail Page (`.article-detail`)
- Full-width article container with fade-in animation
- Structured header with title and metadata
- Highlighted subtitle section with left border accent
- Rich typography for body content
- Back navigation with hover animation

### Navigation
- Sticky header with subtle shadow
- Smooth color transitions on hover
- Full-width with centered container

### Buttons (`.btn`)
- Multiple variants: primary, secondary, accent
- Size options: default, small (`.btn-sm`), large (`.btn-lg`)
- Smooth hover effects with lift and shadow

### Badges (`.badge`)
- Color variants: default, primary, success, warning, danger
- Compact inline elements with pill shape

### Grid System
- CSS Grid for responsive layouts
- Classes: `.grid-cols-1`, `.grid-cols-2`, `.grid-cols-3`, `.grid-cols-4`
- Auto-responds to mobile (single column at 768px breakpoint)

## Animation Patterns

All animations use CSS transitions for smooth, performant effects:

1. **Lift Effects**: Cards and buttons lift slightly on hover (`translateY(-4px)` to `-8px`)
2. **Color Transitions**: All color changes animate smoothly
3. **Fade In**: Article detail pages fade in on load
4. **Loading State**: Skeleton loaders use gradient animation

## Responsive Breakpoints

- **Desktop**: Full layout (default)
- **Tablet**: 768px - Grid and spacing adjustments
- **Mobile**: 480px - Further optimizations for small screens

## Usage in Templates

All styles use semantic HTML with utility classes:

```html
<!-- Article Card -->
<a href="#" class="article-card">
  <div class="article-card-content">
    <div class="article-card-header">
      <h2 class="article-card-title">Title</h2>
      <p class="article-card-subtitle">Subtitle</p>
    </div>
    <div class="article-card-body">
      <p class="article-card-excerpt">Excerpt text...</p>
    </div>
    <div class="article-card-footer">
      <div class="article-card-meta">
        <span class="article-card-date">Date</span>
        <span class="badge badge-primary">Label</span>
      </div>
    </div>
  </div>
</a>

<!-- Button -->
<a href="#" class="btn btn-primary btn-lg">Call to Action</a>

<!-- Grid -->
<div class="articles-grid">
  <!-- Items automatically distribute -->
</div>
```

## Customization

### Modify Colors
Edit `variables.css` under the `:root` selector:
```css
--color-primary: #your-color;
--color-secondary: #your-color;
```

### Adjust Spacing
Update spacing variables (8px base unit):
```css
--spacing-base: 1rem; /* Change base unit here */
```

### Customize Transitions
Modify transition speeds:
```css
--transition-fast: 150ms ease-in-out;
--transition-base: 250ms ease-in-out;
--transition-slow: 350ms ease-in-out;
```

## Best Practices

1. **Use CSS Variables**: Always reference variables instead of hardcoding values
2. **Mobile First**: Styles apply mobile-first, breakpoints add complexity
3. **Semantic HTML**: Use proper heading hierarchy and semantic elements
4. **Accessibility**: Maintain color contrast ratios (WCAG AA minimum)
5. **Performance**: CSS is minimal and efficient, avoiding unnecessary animations

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- CSS Grid and Flexbox supported
- CSS Variables supported in all modern browsers
- Fallbacks provided for older browsers where necessary

## Future Enhancements

Consider adding:
- Dark mode toggle using CSS variables
- Additional component variants
- Animation preferences (prefers-reduced-motion)
- Additional typography scales for different languages
