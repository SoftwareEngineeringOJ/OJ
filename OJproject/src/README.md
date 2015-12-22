##关于mysubmitcode.html
###修改前
<option value="all">All</option>
<option value="c">C</option>
<option value="c++">C++</option>
<option value="c#">C#</option>
<option value="python">Python</option>
<option value="java">Java</option>
<option value="pascal">Pascal</option>
<option value="ruby">Ruby</option>
###修改后
{% for l in lan %}
<option value="{{ l }}">{{ l }}</option>
{% endfor %}
