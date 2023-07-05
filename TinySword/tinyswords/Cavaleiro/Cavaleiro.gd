extends KinematicBody2D
onready var ataque:CollisionShape2D = get_node("AreaAtaque/colisaoAtaque")
onready var animacao:AnimationPlayer= get_node("AnimationPlayer")
onready var textura:Sprite = get_node("Textura")	
onready var aux_animation:AnimationPlayer = get_node("AnimationAux") 

export var move_speed:float = 256.0
export var damage:int = 3
export var health:int = 10
var pode_morrer =false

var velocity:Vector2
var pode_atacar:bool = true
func  get_direction()-> Vector2:
	return Vector2(
		Input.get_axis("mover_es","mover_dir"),
		Input.get_axis("mover_up","mover_down")
	).normalized()

func _physics_process(delta:float)-> void:
	if( pode_atacar==false or pode_morrer):
		return
	move()
	animate()
	handlerAtaque()
func move()->void:
	var direction:Vector2 = get_direction()
	velocity = direction * move_speed
	move_and_slide(velocity,direction)

func animate()->void:	
	if velocity.x > 0:
		textura.flip_h = false
		ataque.position.x = 58#28
	if velocity.x < 0:
		textura.flip_h = true
		ataque.position.x = -58#28
	if velocity!=Vector2.ZERO:
		animacao.play("Correndo")
		return 
	animacao.play("parado")
	
func handlerAtaque()-> void:
	if Input.is_action_just_pressed("Ataque") and pode_atacar:
		pode_atacar = false
		animacao.play("Ataque")
		
		

func _on_AnimationPlayer_animation_finished(_anim_name:String)->void:
	match _anim_name:
		"Ataque": 
			pode_atacar = true
		"Morte":
			get_tree().reload_current_scene()

func update_health(value:int)->void:
	health-=value
	if health < 0:
		pode_morrer = true
		animacao.play("Morte")
		ataque.disabled =true
		return 
	aux_animation.play("hit")
	
	
func _on_AreaAtaque_body(body)->void:
	body.update_health(damage)
