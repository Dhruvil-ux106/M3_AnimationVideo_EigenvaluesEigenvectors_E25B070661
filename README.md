# Eigenvalues & Eigenvectors – Understanding Matrix Transformations Visually
**Course:** Linear Algebra and Calculus (M3) – Internal Assessment (Project Option 1)  
**Student Name:** Dhruvil Kamlesh Shah  
**URN No.:** E25B070661  

## Learning Objective
By the end of this visual guide, viewers can define eigenvalues and eigenvectors, interpret $A\vec{v} = \lambda\vec{v}$ geometrically on a 2D coordinate grid, compute eigenvalues via $\det(A - \lambda I) = 0$, solve for corresponding eigenvectors, and verify results geometrically.

## Repository Contents
- `EigenvaluesEigenvectors_Video.mp4`: Final 1080p (1920×1080) 16:9 narrated & subtitled animation.
- `_Code/eigenvalues_eigenvectors.py`: Complete modular Manim Community Edition Python source code.
- `Storyboard.pdf`: 6-scene visual, mathematical, and narration plan.

## Installation & Execution (macOS)
1. Install dependencies: `brew install py3cairo ffmpeg pango pkg-config` and `brew install --cask basictex`
2. Set up Python environment: `python3 -m venv venv && source venv/bin/activate && pip install manim`
3. Render video: `manim -pqh _Code/eigenvalues_eigenvectors.py FullEigenvaluesProject`

## Credits & AI Disclosure
- **References:** Gilbert Strang, *Introduction to Linear Algebra*; Grant Sanderson (3Blue1Brown), *Essence of Linear Algebra*.
- **AI Disclosure:** AI assistance was used to structure the Manim Python animation code, storyboard layout, and voice-over script pacing. All mathematical derivations and visual outputs were independently verified.
