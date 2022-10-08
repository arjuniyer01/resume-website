page_setup = f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 25rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 25rem;}}
        div.stDownloadButton > button:first-child {{background-color: #000000; color:#FFFFFF; border-radius: 10px; padding: 10px; font-weight: bold;}}  
        div.stDownloadButton > button:hover {{border-width: thick;}}
    </style>
'''

embed_component = {
    "linkedin": """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="dark" data-type="HORIZONTAL" data-vanity="arjun-iyer-4b6412196" data-version="v1"></div>
              """,
    "github": '<script type="module" src="https://unpkg.com/@rocktimsaikia/github-card@latest?module"></script><div class="github-card" data-width="500"><github-card data-user="arjuniyer01" data-theme="dark" data-height="1000"></github-card></div',
}

repository_embed = {
    'Python' : {
        'Pneumonia_Detector': '[![arjuniyer01/Pneumonia_Detector - GitHub](https://gh-card.dev/repos/arjuniyer01/Pneumonia_Detector.svg)](https://github.com/arjuniyer01/Pneumonia_Detector)',
    'resume-website': '[![arjuniyer01/resume-website - GitHub](https://gh-card.dev/repos/arjuniyer01/resume-website.svg)](https://github.com/arjuniyer01/resume-website)',
    },
    'C': {
        'neural-network-from-scratch': '[![arjuniyer01/neural-network-from-scratch - GitHub](https://gh-card.dev/repos/arjuniyer01/neural-network-from-scratch.svg)](https://github.com/arjuniyer01/neural-network-from-scratch)',
        'Memory_Allocator': '[![arjuniyer01/Memory_Allocator - GitHub](https://gh-card.dev/repos/arjuniyer01/Memory_Allocator.svg)](https://github.com/arjuniyer01/Memory_Allocator)',
    },
    'Java': {
        'WikipediaTermSearch': '[![arjuniyer01/WikipediaTermSearch - GitHub](https://gh-card.dev/repos/arjuniyer01/WikipediaTermSearch.svg)](https://github.com/arjuniyer01/WikipediaTermSearch)',
    'BestFlight': '[![arjuniyer01/BestFlight - GitHub](https://gh-card.dev/repos/arjuniyer01/BestFlight.svg)](https://github.com/arjuniyer01/BestFlight)',
    },
    'R': {
        'Instant_Body_Fat': '[![arjuniyer01/Instant_Body_Fat - GitHub](https://gh-card.dev/repos/arjuniyer01/Instant_Body_Fat.svg)](https://github.com/arjuniyer01/Instant_Body_Fat)',
    },
    'Bash': {},
    'TypeScript': {},
    'SQL': {},
}

lang_chart = {
    "click": "function(params) { console.log(params.name) }",
    "toolbox": {
        "show": True,
        "feature": {
            "mark": {"show": True},
        },
    },
    "series": [
        {
            "type": "pie",
            "radius": [30, 150],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": 10, "name": "Python"},
                {"value": 9, "name": "C"},
                {"value": 8, "name": "Java"},
                {"value": 7, "name": "TypeScript"},
                {"value": 8, "name": "SQL"},
                {"value": 8, "name": "R"},
                {"value": 7, "name": "Bash"},
            ],
        }
    ],
}