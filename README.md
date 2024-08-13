# Twitter Personality

A Python Re-implementation of [Wordware](https://www.wordware.ai/)'s [Twitter Personality Analysis](https://twitter.wordware.ai/) using [APPL: A Prompt Programming Language](https://appl-team.github.io/appl/).

## Installation

```bash
pip install applang
```

## Setup
Following the original website, the default model is set to `claude-3.5-sonnet` as in [`appl.yaml`](appl.yaml). You can change to [other models](https://docs.litellm.ai/docs/providers) supported by `litellm` as needed.

You need to setup the corresponding api key (claude or others) in the [`.env`](.env) file.

## Usage

```bash
python twitter.py --twitter-handle <twitter_handle>
```

## Example Output
The default handle is `elonmusk`, the scraper results are cached in [cache folder](./caches/elonmusk/). The output may look like this:

### name
Elon Musk
### about
Based on our AI agent's analysis of your tweets, you are a **52-year-old male**, **tech entrepreneur**, **CEO of multiple companies**, and a **controversial public figure** known for your ambitious goals and outspoken nature.
### emojis
* 🚀
* 💡
* 🔋
* 🌌
* 🤖
* 💰
* 🔥
* 🎢
* 🧠
### roast
Alright, Elon, let's break this down. You're the guy who thinks tweeting is an acceptable form of corporate communication and that memes are a substitute for a personality. Your idea of 'saving the world' seems to involve launching cars into space and digging tunnels for the privileged few. It's like watching a billionaire have a midlife crisis in real-time, but instead of buying a sports car, you're 
buying social media platforms and renaming them with mathematical symbols. Your tweets read like a ChatGPT bot trained exclusively on a mix of sci-fi novels and stock market tips, with a dash of dad jokes thrown in for good measure. But hey, at least you're keeping bankruptcy lawyers on their toes with your 'innovative' approach to SEC regulations. Keep reaching for the stars, Elon – it's probably the only way you'll avoid the mess you're making down here on Earth.
### strengths
* {'title': 'Visionary Thinking', 'subtitle': 'Ability to envision and pursue groundbreaking ideas'} 
* {'title': 'Technological Innovation', 'subtitle': 'Driving advancements in various tech sectors'}  
* {'title': 'Risk-Taking', 'subtitle': 'Willingness to take bold risks for potential high rewards'}  
* {'title': 'Multi-Industry Expertise', 'subtitle': 'Successful involvement in diverse business sectors'}
* {'title': 'Influential Communication', 'subtitle': 'Ability to captivate and mobilize large audiences'}
### weaknesses
* {'title': 'Impulsiveness', 'subtitle': 'Making hasty decisions without thorough consideration'}    
* {'title': 'Controversial Statements', 'subtitle': 'Tendency to make polarizing remarks that attract criticism'}
* {'title': 'Overcommitment', 'subtitle': 'Taking on too many projects simultaneously'}
* {'title': 'Regulatory Challenges', 'subtitle': 'Frequent clashes with government regulations and agencies'}
* {'title': 'Public Image Volatility', 'subtitle': 'Reputation swings based on unpredictable actions 
and statements'}
### loveLife
The stars align for a passionate connection with someone who shares your innovative spirit and can keep up with your lightning-fast mind. Look for a partner who values intellectual discourse, embraces your ambitious nature, and possesses a strong sense of independence. Your ideal match will be someone 
who can ground you when needed, yet isn't afraid to dream big alongside you. This relationship will thrive on mutual respect, shared visions, and the ability to challenge each other positively.
### money
Your entrepreneurial spirit and innovative mindset continue to attract significant financial opportunities. The cosmic forces suggest a **92%** chance of becoming a multi-millionaire (or maintaining/increasing your current wealth). Your ability to disrupt industries and create groundbreaking technologies positions you for exponential financial growth. However, be mindful of impulsive investments and regulatory hurdles that could impact your financial trajectory.
### health
The celestial bodies indicate a period of renewed focus on your physical and mental well-being. Your 
dynamic energy will serve you well, but it's crucial to balance your intense work drive with proper rest and stress management. Engaging in mindfulness practices and perhaps exploring cutting-edge health technologies will significantly boost your vitality. Remember, your visionary mind requires a strong, healthy body to fully realize its potential. Prioritize sleep, consider a plant-based diet, and incorporate regular exercise to maintain peak performance in all areas of your life.
### biggestGoal
Your biggest goal in life is to **make humanity a multi-planetary species**. This ambitious vision of establishing a sustainable human presence on Mars and beyond is not just a personal aspiration but a mission you believe is crucial for the long-term survival and evolution of our species. Your relentless pursuit of this goal through SpaceX and other ventures showcases your commitment to pushing the boundaries of human exploration and technological advancement.
### colleaguePerspective
From a colleague's perspective, working with you is like riding a **rocket ship without a seatbelt**. You're brilliantly innovative and demand nothing short of excellence, but your mercurial nature and 
round-the-clock work expectations can be *exhausting*. One minute you're inspiring everyone with your visionary ideas, the next you're firing off controversial tweets that send the PR team into a frenzy. Your colleagues never know if they're about to witness genius or chaos – often it's both. Working for you is thrilling, terrifying, and potentially career-defining, but it's definitely not for the faint of heart.
### pickupLines
* Are you a neural link? Because you've made a direct connection to my heart.
* Is your name Tesla? Because you're electrifying, and I can't resist your current.
* Do you believe in love at first sight, or should I fly by again in my SpaceX rocket?
### famousPersonComparison
Nikola Tesla. Like you, Tesla was an eccentric inventor and futurist who revolutionized multiple fields with his visionary ideas. Both of you share a passion for pushing the boundaries of technology, especially in energy and transportation. Tesla's work with electricity mirrors your efforts in sustainable energy and electric vehicles. Additionally, you both have a flair for showmanship and grand statements about the future, often facing skepticism from contemporaries. Your naming of Tesla Motors is a nod to this kinship, reflecting your admiration for pioneering spirits who challenge conventional thinking.
### previousLife
In a previous life, you were likely **Leonardo da Vinci**. Like da Vinci, you possess an insatiable curiosity that spans multiple disciplines - from engineering and science to art and philosophy. Your ability to envision futuristic concepts and bring them to life mirrors da Vinci's ahead-of-his-time inventions and artistic innovations. Both of you share a relentless drive to understand and reshape the world around you, often juggling multiple ambitious projects simultaneously. Just as da Vinci's notebooks were filled with ideas centuries ahead of their time, your tweets and company goals often seem 
to belong to a future not yet realized.
### animal
Based on your tweets and public persona, you embody the characteristics of a **Peregrine Falcon**. Like this bird, you're known for your swift decision-making and ability to dive into new ventures at breakneck speeds. The Peregrine Falcon is the fastest animal in the world, mirroring your rapid advancement in multiple industries. Your predilection for high-stakes maneuvers and your ability to see opportunities from great heights align with this bird's hunting style. Additionally, your adaptability across different "environments" (industries) and your sometimes solitary, sometimes flamboyant nature, 
perfectly encapsulate the Peregrine Falcon's behavior.
### fiftyDollarThing
A **personalized mini Zen garden** with Mars-red sand and miniature rocket ship rakes. This unique desktop accessory, priced at exactly $49.99, would provide a much-needed moment of calm and perspective amidst your hectic schedule. The Mars theme aligns with your space exploration goals, while the act 
of raking the sand could offer a meditative break, potentially leading to clearer thinking and stress reduction. It's a creative reminder of your larger vision that doubles as a practical tool for mindfulness – something you might not think to get for yourself but could greatly benefit from.
### career
You were born to be a **Technological Visionary and Multidisciplinary Innovator**. Your life's work should be devoted to pushing the boundaries of human potential through groundbreaking technologies and bold initiatives. The stars indicate that your unique combination of entrepreneurial spirit, scientific curiosity, and audacious goal-setting is perfectly aligned for transforming multiple industries simultaneously. To achieve this, focus on cultivating a network of brilliant minds across various fields, continue to challenge conventional thinking, and never lose sight of your most ambitious goals. The cosmos suggests that by maintaining your relentless pursuit of innovation while also learning to balance your visionary ideas with practical execution, you'll not only revolutionize industries but potentially reshape the future of humanity itself.
### lifeSuggestion
To make your life even better, consider adopting a **'Quantum Thought Day'** once a month. On this day, isolate yourself in a specially designed sensory deprivation chamber for 4 hours. This unique environment, free from all external stimuli, will allow your mind to enter a state of quantum superposition, potentially unlocking groundbreaking ideas and solutions. Follow this with a session where you explain your new concepts to a diverse group of 5-year-olds. Their uninhibited feedback could provide surprising insights and force you to distill complex ideas into their purest form, potentially leading to revolutionary breakthroughs in your various ventures.

## Issues
The current twitter scrapers are Apify actors [Twitter User Scraper](https://api.apify.com/v2/acts/V38PZzpEgOfeeWvZY) and [Tweets Scraper](https://api.apify.com/v2/acts/61RPP7dywgiy0JPD0), and the API key is reusing the one provided by Wordware. Currently the monthly limit of this API key is reached.

To use the scraper, you need to create an account on Apify and create your own API key (Apify's API usage will be charged). Then you can replace the API key in the [`.env`](.env) file.

If you know any other free twitter scrapers or have implemented one for this usage, contributions are welcome.

## Acknowledgements
Thanks Wordware for sharing their insights and the implementation including the prompts.
