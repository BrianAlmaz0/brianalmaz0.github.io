# REFLECTION.md

## Task 4: Reflection & AI Attribution

### 1) Flexbox direction: row vs column (in plain words)

Row (the default)
- Think of laying items out left-to-right — that's `flex-direction: row`.
- It's the natural choice for desktop navigation bars and any horizontal layout.

Example from this site:
```css
nav ul {
    display: flex;
    /* items flow left-to-right by default */
    gap: 2rem;
}
```

Column
- Stacks items top-to-bottom. Use this when you want a vertical list (mobile menus are a good example).

Example used on mobile:
```css
@media (max-width: 768px) {
    nav ul {
        flex-direction: column; /* stack links vertically */
        gap: 0.5rem;
    }
}
```

Why it matters: switching between `row` and `column` with media queries is a simple, reliable way to make layouts adapt between wide screens and narrow screens.

---

### 2) Why I prefer relative units (rem, %, vh) over fixed pixels

Short answer: relative units scale, pixels don't.

Example problem with pixels:
```css
header h1 { font-size: 40px; padding: 20px; }
```
On a phone that `40px` might be too large and make the page feel cramped.

How relative units help:
- `rem` scales based on the root font size. `2rem` is easy to reason about and respects user preferences.
- `%` and `width: 100%` make elements adapt to their container.
- `vh` is handy when you want something to relate to viewport height (e.g., a full-screen hero).

In this project I used things like `gap: 2rem` and `width: 100%` for images so the layout adapts across screen sizes.

---

### 3) AI attribution — how I used AI and why I didn't just hand the project off

Tools I used: GitHub Copilot and Claude (Anthropic).

I used AI as a tutor and sounding board. I asked conceptual questions and used the answers to make informed decisions. Here are some of prompts I used:

- "How does `justify-content: space-between` work in a flex container, and when should I use it for a header?" — helped me figure out how to space logo and nav links.
- "What's the advantage of `grid-template-columns: repeat(3, 1fr)` over fixed column widths for a project gallery?" — helped me choose `1fr` for a flexible 3-column grid.
- "When should I use `rem` vs `px`? Show an example where `rem` adapts better." — clarified unit choices.

What I changed after AI suggestions:
- The AI suggested `grid-gap: 2rem`; I used the modern `gap: 2rem` instead.

What AI helped me do:
- Understand trade-offs and best practices
- Get quick explanations of CSS concepts so I could decide what to implement
- Iterate faster by testing ideas it suggested and adjusting them to fit my site

---

Assignment completion: March 8, 2026
Student: Brian Almazo
Repository: https://github.com/BrianAlmaz0/brianalmaz0.github.io
