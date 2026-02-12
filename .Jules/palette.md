## 2025-05-15 - Redundant Screen Reader Announcements
**Learning:** When adding a descriptive `aria-label` to an anchor tag that contains an icon image, keeping the `alt` text on the image results in redundant announcements by screen readers (e.g., "Link, Facebook, Image, Facebook").
**Action:** Set the image `alt` attribute to an empty string (`alt=""`) when the parent link has a sufficient `aria-label`.
