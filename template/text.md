<ul class="navbar-nav mx-auto" style="gap: 8px;">
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'home' %}active{% endif %}" href="{% url 'home' %}">Home</a>
  </li>
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'our_firm' %}active{% endif %}" href="{% url 'our_firm' %}">Our Firm</a>
  </li>
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'investment_model' %}active{% endif %}" href="{% url 'investment_model' %}">Investment Model</a>
  </li>
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'business_owners' %}active{% endif %}" href="{% url 'business_owners' %}">For Business Owners</a>
  </li>
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'investors' %}active{% endif %}" href="{% url 'investors' %}">For Investors</a>
  </li>
</ul>