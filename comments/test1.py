<ul class="media-list">
        {% recursetree comments_list %}
        <li class="media">
            <a class="media-left" href="#" id="c{{ node.pk }}">
                {% if node.user.social_avatar  %}
                <img width="30px" height="30px" alt="{{ node.user.username }}" src="{{ node.user.social_avatar  }}">
                {% else %}
                <img class="media-object" src="{% static 'blog/images/author.svg' %}" alt="{{ node.user.username }}">
                {% endif %}
            </a>
            <div class="media-body">
                <h4 class="media-heading">
                        {{node.user}}
                </h4>
                <p>
                    {{node.content|safe}}
                </p>
                <p>
                    {{node.created_time|timesince}} 之前.<a href="{% url 'comments:reply' node.pk %}">回复</a>
                </p>             
                {% if not node.is_leaf_node %}
                <!-- 嵌套的媒体对象 -->
                <ul class="media-list">
                    
                    {{ children }}
                    
                </ul>
                {% endif %}
            </div>
        </li>
        {% endrecursetree %}
 </ul>
