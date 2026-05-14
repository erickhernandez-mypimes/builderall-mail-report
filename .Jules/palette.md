## 2025-05-15 - Interactive states and social link accessibility in email templates

**Learning:** Email templates in this repository (Fundación Mundo Mujer) frequently define CSS transitions for CTA buttons but lack the corresponding `:hover` pseudo-class. Additionally, social media icons in footers are often missing descriptive accessibility attributes, which is critical for screen reader users and provides useful tooltips for all users.

**Action:** When working with email templates, always verify that interactive elements like buttons have explicit `:hover` states if transitions are defined. Ensure all icon-only social links include both `aria-label` and `title` attributes in the template's language (Spanish) to maximize accessibility and usability.
