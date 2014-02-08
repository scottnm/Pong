using UnityEngine;
using System.Collections;

public class PlayerController : MonoBehaviour {
	
	public enum Player { Player1, Player2 };
	public Player player;
	
	private float speed = 6f;
	
	void FixedUpdate () {
		string playerString = player == Player.Player1 ? "P1" : "P2";
		float direction = Input.GetAxis("Vertical-" + playerString);
		rigidbody2D.velocity = new Vector2(0, speed * direction);

		Vector3 pos = transform.position;
		pos.y = pos.y < -3.3f ? -3.3f : pos.y;
		pos.y = pos.y > 3.3f ? 3.3f : pos.y;
		transform.position = pos;
	}
}
