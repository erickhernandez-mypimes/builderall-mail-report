## 2025-05-15 - Accessibility for Social Media Links in Email Templates
**Learning:** Icon-only social media links in email footers are common in this repository but often lack descriptive attributes. In a Spanish-language context, providing both `title` (for mouse hover tooltips) and `aria-label` (for screen readers) in Spanish is critical for a truly accessible and professional user experience.
**Action:** Always scan for social media icon links and ensure they have `title` and `aria-label` attributes that clearly describe the destination (e.g., 'Facebook de Fundación Mundo Mujer').

## 2025-05-15 - Interactive Feedback in Email Templates
**Learning:** Users expect interactive elements like CTA buttons to provide visual feedback. While email clients have varying support for CSS, implementing a `:hover` state in a `<style>` block is a low-cost, high-impact micro-UX improvement for modern email clients.
**Action:** Ensure all `.cta-button` elements have a defined `:hover` state with an appropriate brand-aligned color and a smooth transition.
