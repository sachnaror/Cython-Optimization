# Cython Optimization

Cython can significantly speed up parts of your application that are computationally intensive, but it also adds complexity to your build process and requires maintaining code in a language that is slightly different from Python.

Identify a part of your application that is computation-heavy. This could be a section of your recommendation algorithm, data processing, or another suitable aspect. Implement this part in Cython, and integrate it with your Django application.

## Deployment

To deploy this project run

```
pip install cython
python setup.py build_ext --inplace

```

--------------


<img width="532" alt="Screenshot 2024-02-27 at 4 54 17 AM" src="https://github.com/sachnaror/Cython-Optimization/assets/9551754/2135f11e-e7af-4de2-96c5-38480fcf7373">
