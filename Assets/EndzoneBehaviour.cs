using UnityEngine;
using System.Collections;

public class EndzoneBehaviour : MonoBehaviour {
	
	public PlayerController.Player player;
	
	void OnTriggerEnter2D(Collider2D collider) {
		if(collider.tag == "Ball") {
			if(player == PlayerController.Player.Player1) {
				State.p1Score++;
				collider.GetComponent<BallController>().Reset(PlayerController.Player.Player2);
			} else {
				State.p2Score++;
				collider.GetComponent<BallController>().Reset(PlayerController.Player.Player1);
			}
		}
		
	}
}
