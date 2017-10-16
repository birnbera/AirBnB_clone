<h1 class="gap">0x01. AirBnB clone - Web static</h1>


<h4 class="task">
    0. Inline styling
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header and a footer.</p><p>Layout:</p><ul>
<li>Body:

<ul>
<li>no margin</li>
<li>no padding</li>
</ul></li>
<li>Header:

<ul>
<li>color #FF0000 (red)</li>
<li>height: 70px</li>
<li>width: 100%</li>
</ul></li>
<li>Footer:

<ul>
<li>color #00FF00 (green)</li>
<li>height: 60px</li>
<li>width: 100%</li>
<li>text <code>Holberton School</code> center vertically and horizontally</li>
<li>always at the bottom at the page</li>
</ul></li>
</ul><p>Requirements:</p><ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>You are not allowed to import any files</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>Use inline styling for all your tags</li>
</ul><p><img alt="0-index" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/0-index.png"/></p>


<h4 class="task">
    1. Head styling
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header and a footer by using the <code>style</code> tag in the <code>head</code> tag (same as <code>0-index.html</code>)</p><p>Requirements:</p><ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>You are not allowed to import any files</li>
<li>No inline styling</li>
<li>You must use the <code>style</code> tag in the <code>head</code> tag</li>
</ul><p>The layout must be exactly the same as <code>0-index.html</code></p>


<h4 class="task">
    2. CSS files
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header and a footer by using CSS files (same as <code>1-index.html</code>)</p><p>Requirements:</p><ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>No inline styling</li>
<li>You must have 3 CSS files:

<ul>
<li><code>styles/2-common.css</code>: for global style (i.e. the <code>body</code> style)</li>
<li><code>styles/2-header.css</code>: for header style</li>
<li><code>styles/2-footer.css</code>: for footer style</li>
</ul></li>
</ul><p>The layout must be exactly the same as <code>1-index.html</code></p>


<h4 class="task">
    3. Zoning done!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header and footer by using CSS files (same as <code>2-index.html</code>)</p><p>Layout:</p><ul>
<li>Common:

<ul>
<li>no margin</li>
<li>no padding</li>
<li>font color: #484848</li>
<li>font size" 14px</li>
<li>font family: <code>Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;</code></li>
<li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png" target="_blank" title="icon">icon</a> in the browser tab</li>
</ul></li>
<li>Header:

<ul>
<li>color: white</li>
<li>height: 70px</li>
<li>width: 100%</li>
<li>border bottom 1px #CCCCCC</li>
<li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png" target="_blank" title="logo">logo</a> align on left and center vertically (20px space at the left)</li>
</ul></li>
<li>Footer:

<ul>
<li>color white</li>
<li>height: 60px</li>
<li>width: 100%</li>
<li>border top 1px #CCCCCC</li>
<li>text <code>Holberton School</code> center vertically and horizontally</li>
<li>always at the bottom at the page</li>
</ul></li>
</ul><p>Requirements:</p><ul>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 3 CSS files:

<ul>
<li><code>styles/3-common.css</code>: for the global style (i.e <code>body</code> style)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
</ul></li>
</ul><p><img alt="3-index" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/3-index.png"/></p>


<h4 class="task">
    4. Search!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header, footer and a filters box with a search button.</p><p>Layout: (based on <code>3-index.html</code>)</p><ul>
<li>Container:

<ul>
<li>between <code>header</code> and <code>footer</code> tags, add a <code>div</code>:

<ul>
<li>classname: <code>container</code></li>
<li>max width 1000px</li>
<li>margin top and bottom 30px</li>
<li>center horizontally</li>
</ul></li>
</ul></li>
<li>Filter section: 

<ul>
<li>tag <code>section</code></li>
<li>classname <code>filters</code></li>
<li>inside the <code>.container</code></li>
<li>color white</li>
<li>height: 70px</li>
<li>width: 100% of the container</li>
<li>border 1px #DDDDDD with radius 4px</li>
</ul></li>
<li>Button search:

<ul>
<li>tag <code>button</code></li>
<li>text <code>Search</code></li>
<li>font size: 18px</li>
<li>inside the section filters</li>
<li>color #FF5A5F</li>
<li>height: 48px</li>
<li>width: 20% of the section filters</li>
<li>no borders</li>
<li>border radius: 4px</li>
<li>center vertically and at 30px of the right border</li>
<li>change opacity to 90% when the mouse is on the button</li>
</ul></li>
</ul><p>Requirements:</p><ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>button</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 4 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (<code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
<li><code>styles/4-filters.css</code>: for the filters style</li>
</ul></li>
<li><code>4-index.html</code> <strong>won’t be W3C valid</strong>, don’t worry, it’s temporary</li>
</ul><p><img alt="4-index" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/4-index.png"/></p>


<h4 class="task">
    5. More filters
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header, footer and a filters box.</p><p>Layout: (based on <code>4-index.html</code>)</p><ul>
<li>Locations and Amenities filters:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>locations</code> for location tag and <code>amenities</code> for the other</li>
<li>inside the section filters (same level as the <code>button</code> Search)</li>
<li>height: 100% of the section filters</li>
<li>width: 25% of the section filters</li>
<li>border right #DDDDDD 1px only for the first left filter</li>
<li>contains a title:

<ul>
<li>tag: <code>h3</code></li>
<li>font weight: 600<br/></li>
<li>text <code>States</code> or <code>Amenities</code></li>
</ul></li>
<li>contains a subtitle:

<ul>
<li>tag: <code>h4</code></li>
<li>font weight: 400<br/></li>
<li>font size: 14px</li>
<li>text with fake contents</li>
</ul></li>
</ul></li>
</ul><p>Requirements:</p><ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>button</code>, <code>h3</code>, <code>h4</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 4 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (<code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
<li><code>styles/5-filters.css</code>: for the filters style</li>
</ul></li>
</ul><p><img alt="5-index" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/5-index.png"/></p>


<h4 class="task">
    6. It's (h)over
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header, footer and a filters box with dropdown.</p><p>Layout: (based on <code>5-index.html</code>)</p><ul>
<li>Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter <code>div</code>: 

<ul>
<li>tag <code>ul</code></li>
<li>classname <code>popover</code></li>
<li>text should be fake now</li>
<li>inside each <code>div</code></li>
<li>not displayed by default</li>
<li>color #FAFAFA</li>
<li>width same as the <code>div</code> filter</li>
<li>border #DDDDDD 1px with border radius 4px</li>
<li>no list display</li>
<li>Location filter has 2 levels of <code>ul</code>/<code>li</code>:

<ul>
<li>state -&gt; cities</li>
<li>state name must be display in a <code>h2</code> tag (font size 16px)</li>
</ul></li>
</ul></li>
</ul><p>Requirements:</p><ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>button</code>, <code>h3</code>, <code>h4</code>, <code>ul</code>, <code>li</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 4 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (<code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
<li><code>styles/6-filters.css</code>: for the filters style</li>
</ul></li>
</ul><p><img alt="6-index_0" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/6-index_0.png">
<img alt="6-index_1" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/6-index_1.png"/></img></p>


<h4 class="task">
    7. Display results
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header, footer, a filters box with dropdown and results.</p><p>Layout: (based on <code>6-index.html</code>)</p><ul>
<li>Add Places section:

<ul>
<li>tag: <code>section</code></li>
<li>classname: <code>places</code></li>
<li>same level as the filters section, inside <code>.container</code></li>
<li>contains a title:

<ul>
<li>tag: <code>h1</code></li>
<li>text: <code>Places</code></li>
<li>align in the top left</li>
<li>font size: 30px</li>
</ul></li>
<li>contains multiple “Places” as listing (horizontal or vertical) describe by:

<ul>
<li>tag: <code>article</code></li>
<li>width: 390px</li>
<li>padding and margin 20px</li>
<li>border #FF5A5F 1px with radius 4px</li>
<li>contains the place name:

<ul>
<li>tag: <code>h2</code></li>
<li>font size: 30px</li>
<li>center horizontally</li>
</ul></li>
</ul></li>
</ul></li>
</ul><p>Requirements:</p><ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>article</code>, <code>button</code>, <code>h1</code>, <code>h2</code>, <code>h3</code>, <code>h4</code>, <code>ul</code>, <code>li</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 5 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (i.e. <code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for footer style</li>
<li><code>styles/6-filters.css</code>: for the filters style</li>
<li><code>styles/7-places.css</code>: for the places style</li>
</ul></li>
</ul><p><img alt="7-index" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/7-index.png"/></p>


<h4 class="task">
    8. More details
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.</p><p>Layout: (based on <code>7-index.html</code>)</p><p>Add more information to a Place <code>article</code>:</p><ul>
<li>Price by night:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>price_by_night</code></li>
<li>same level as the place name</li>
<li>font color: #FF5A5F</li>
<li>border: #FF5A5F 4px rounded</li>
<li>min width: 60px</li>
<li>height: 60px</li>
<li>font size: 30px</li>
<li>align: the top right (with space)</li>
</ul></li>
<li>Information section:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>information</code></li>
<li>height: 80px</li>
<li>border: top and bottom #DDDDDD 1px</li>
<li>contains (align vertically):

<ul>
<li>Number of guests:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>max_guest</code></li>
<li>width: 100px</li>
<li>fake text</li>
<li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png" target="_blank" title="icon">icon</a></li>
</ul></li>
<li>Number of bedrooms:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>number_rooms</code></li>
<li>width: 100px</li>
<li>fake text</li>
<li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png" target="_blank" title="icon">icon</a></li>
</ul></li>
<li>Number of bathrooms:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>number_bathrooms</code></li>
<li>width: 100px</li>
<li>fake text</li>
<li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png" target="_blank" title="icon">icon</a></li>
</ul></li>
</ul></li>
</ul></li>
<li>User section:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>user</code></li>
<li>text <code>Owner: &lt;fake text&gt;</code></li>
<li><code>Owner</code> text should be in bold</li>
</ul></li>
<li>Description section:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>description</code></li>
</ul></li>
</ul><p>Requirements:</p><ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>article</code>, <code>button</code>, <code>h1</code>, <code>h2</code>, <code>h3</code>, <code>h4</code>, <code>ul</code>, <code>li</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 5 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (i.e. <code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
<li><code>styles/6-filters.css</code>: for the filters style</li>
<li><code>styles/8-places.css</code>: for the places style</li>
</ul></li>
</ul><p><img alt="8-index" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png"/></p>
