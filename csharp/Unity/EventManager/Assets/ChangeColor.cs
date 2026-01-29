using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeColor : MonoBehaviour
{
    public Color color;

    void Start()
    {
        EventManager.ExampleEvent += SetNewColor;
    }

    private void SetNewColor()
    {
        GetComponent<SpriteRenderer>().color = color;
    }


    private void OnDisable()
    {
        EventManager.ExampleEvent -= SetNewColor;
    }
}
