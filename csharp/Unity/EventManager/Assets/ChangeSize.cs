using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Income : MonoBehaviour
{
    [SerializeField] int _income;
    [SerializeField] int _timeToIncome;

    public event Action GoldChanged;

    private Cash _cash => GetComponent<Cash>();

    private void Start()
    {
        InvokeRepeating("IncomeTime", 1f, _timeToIncome);
    }

    void IncomeTime ()
    {
        _cash.Gold += _income;
        GoldChanged?.Invoke();
    }
}
