##����mysubmitcode.html
###�޸�ǰ
<option value="all">All</option>
<option value="c">C</option>
<option value="c++">C++</option>
<option value="c#">C#</option>
<option value="python">Python</option>
<option value="java">Java</option>
<option value="pascal">Pascal</option>
<option value="ruby">Ruby</option>
###�޸ĺ�
{% for l in lan %}
<option value="{{ l }}">{{ l }}</option>
{% endfor %}
