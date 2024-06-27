from main import main
from slide_obj import Slide
import json

unformatted = """
  ### Course: The History of Domestication

---

### Slide 1: Introduction to Domestication
- **Bullet Points:**
  - Definition of domestication
  - Brief overview of its historical significance

- **Speaker's Notes:**
  - "Good day, everyone! Today, we're going to explore the fascinating history of domestication—how humans have transformed wild plants and animals into domesticated partners through selective breeding. This process has shaped civilizations and the natural world around us."

- **Suggested Image:**
  - A collage of various domesticated plants and animals

---

### Slide 2: Early Domestication
- **Bullet Points:**
  - Beginning in the Neolithic Era
  - Early domesticated animals: dogs, cattle, and goats
  - Domestication of plants: wheat, rice, and corn

- **Speaker's Notes:**
  - "Domestication started back in the Neolithic Era, a pivotal time when human societies transitioned from hunting and gathering to farming and settling. Early domesticated animals include dogs, which were used for hunting and protection, and livestock like cattle and goats. On the plant side, essentials such as wheat in the Fertile Crescent, rice in Asia, and corn in the Americas began to be cultivated."

- **Suggested Image:**
  - Ancient painting or illustration showing Neolithic farming

---

### Slide 3: Impacts of Domestication
- **Bullet Points:**
  - Agricultural development
  - Growth of civilizations
  - Environmental changes

- **Speaker's Notes:**
  - "The practice of domestication brought about revolutionary changes. It underpinned the development of agriculture, which led to the growth of civilizations and transformed human lifestyles drastically. Moreover, domestication has also had profound impacts on the environment, influencing biodiversity and landscapes."

- **Suggested Image:**
  - Diagram showing the spread of agriculture across the globe

---

### Slide 4: Modern Implications
- **Bullet Points:**
  - Genetic modification and selective breeding
  - Conservation and biodiversity issues
  - The future of domestication

- **Speaker's Notes:**
  - "In modern times, domestication continues to evolve through advanced technologies like genetic modification. While it offers solutions to food security, it also raises important questions about conservation and biodiversity. The future of domestication could redefine our ecological and ethical boundaries."

- **Suggested Image:**
  - A split image depicting traditional farming versus modern genetic modifications

---

### Conclusion and Q&A
- **Invite questions from the audience about the history and future implications of domestication.**
- **Encourage further exploration into how domestication has shaped and will continue to shape our world.**

---

Here is the final JSON structure for your lesson:

```json
{
    "title_page" : [
        {
            "title" : "The History of Domestication"
        }
    ],
    "Slides" : [
        {
            "slide_title" : "Introduction to Domestication",
            "bullet_points" : [
                {
                    "1" : "Definition of domestication",
                    "2" : "Brief overview of its historical significance"
                }
            ],
            "image" : "A collage of various domesticated plants and animals",
            "speakers_note" : "Good day, everyone! Today, we're going to explore the fascinating history of domestication—how humans have transformed wild plants and animals into domesticated partners through selective breeding. This process has shaped civilizations and the natural world around us."
        },
        {
            "slide_title" : "Early Domestication",
            "bullet_points" : [
                {
                    "1" : "Beginning in the Neolithic Era",
                    "2" : "Early domesticated animals: dogs, cattle, and goats",
                    "3" : "Domestication of plants: wheat, rice, and corn"
                }
            ],
            "image" : "Ancient painting or illustration showing Neolithic farming",
            "speakers_note" : "Domestication started back in the Neolithic Era, a pivotal time when human societies transitioned from hunting and gathering to farming and settling. Early domesticated animals include dogs, which were used for hunting and protection, and livestock like cattle and goats. On the plant side, essentials such as wheat in the Fertile Crescent, rice in Asia, and corn in the Americas began to be cultivated."
        },
        {
            "slide_title" : "Impacts of Domestication",
            "bullet_points" : [
                {
                    "1" : "Agricultural development",
                    "2" : "Growth of civilizations",
                    "3" : "Environmental changes"
                }
            ],
            "image" : "Diagram showing the spread of agriculture across the globe",
            "speakers_note" : "The practice of domestication brought about revolutionary changes. It underpinned the development of agriculture, which led to the growth of civilizations and transformed human lifestyles drastically. Moreover, domestication has also had profound impacts on the environment, influencing biodiversity and landscapes."
        },
        {
            "slide_title" : "Modern Implications",
            "bullet_points" : [
                {
                    "1" : "Genetic modification and selective breeding",
                    "2" : "Conservation and biodiversity issues",
                    "3" : "The future of domestication"
                }
            ],
            "image" : "A split image depicting traditional farming versus modern genetic modifications",
            "speakers_note" : "In modern times, domestication continues to evolve through advanced technologies like genetic modification. While it offers solutions to food security, it also raises important questions about conservation and biodiversity. The future of domestication could redefine our ecological and ethical boundaries."
        }
    ]
}
```
"""

def create_json_file():
    json_string = unformatted[unformatted.find("{") : unformatted.rindex("}") + 1]
    data = json.loads(json_string)
    return data


