using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CannonScript : MonoBehaviour
{
    public int speed;
    public float friction;
    public float lerpSpeed;
    float xDegrees;
    float yDegrees;
    Quaternion fromRotation;
    Quaternion toRotation;
    Camera camera;

    public GameObject cannonBall;
    Rigidbody cannonBallRB;
    public Transform shotPosition;
    public GameObject explosion;
    public float firePower;


    void Start()
    {
        camera = Camera.main;
    }

    void Update()
    {
        RaycastHit hit;
        Ray ray = camera.ScreenPointToRay(Input.mousePosition);

        if(Physics.Raycast(ray, out hit)) 
        {
            if (hit.transform.gameObject.tag == "Cannon")
            {
                if (Input.GetMouseButton(0))
                {
                    xDegrees -= Input.GetAxis("Mouse Y") * speed * friction;
                    yDegrees -= Input.GetAxis("Mouse X") * speed * friction;
                    fromRotation = transform.rotation;
                    toRotation = Quaternion.Euler(xDegrees, yDegrees, 0);
                    transform.rotation = Quaternion.Lerp(fromRotation, toRotation, Time.deltaTime * lerpSpeed);

                }
            }
        }
        if (Input.GetMouseButtonDown(1))
        {
            FireCannon();
        }
    }
    public void FireCannon()
    {
        shotPosition.rotation = transform.rotation;
        firePower *= 2000;
        GameObject cannonBallCopy = Instantiate(cannonBall, shotPosition.position, shotPosition.rotation);
        cannonBallRB = cannonBallCopy.GetComponent<Rigidbody>();
        cannonBallRB.AddForce(transform.forward * firePower);
        Instantiate(explosion, shotPosition.position, shotPosition.rotation);
    }
   
}
