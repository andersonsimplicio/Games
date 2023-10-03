extends Node2D

onready var terreno:TileMap = get_node("Grama")
onready var agua:TileMap = get_node("Agua")
var terreno_utlizado:Array

# Called when the node enters the scene tree for the first time.
func _ready()->void:
	var terreno_usado:Rect2 = terreno.get_used_rect()
	terreno_utlizado = terreno.get_used_cells()
	gerador_mar(terreno_usado)

func gerador_mar(terreno:Rect2)->void:
	for x in range(terreno.position.x-14, terreno.size.x+14):
		for y in range(terreno.position.y-14, terreno.size.y+14):
			if terreno_utlizado.has(Vector2(x,y)):
				continue
			agua.set_cell(x,y,0)
#func _process(delta):
#	pass
