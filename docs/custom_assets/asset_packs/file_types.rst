==========
File types
==========

.. _file-type-image:

Image
-----

Supported formats
^^^^^^^^^^^^^^^^^

By default, Tabletop Club supports all of the image formats that Godot supports,
the list of which can be found `here
<https://docs.godotengine.org/en/stable/getting_started/workflow/assets/importing_images.html>`_.


UV Mappings
^^^^^^^^^^^

Every object that uses an image has something called a UV mapping, a way in
which the image is "folded" onto the 3D object. Remember in maths when you had
to "unfold" different shapes into nets? This is essentially the reverse of
that! Knowing these UV mappings is important if you want your object to look
right in-game!

.. note::

   The width and height of the images don't matter, as long as the proportions
   are correct!

Card
""""

.. image:: uv_mappings/card.svg

.. note::

   Unlike other objects, cards use two images, one for each face. See
   :ref:`object-type-card` for more information.

Cube
""""

.. image:: uv_mappings/cube.svg

Cylinder
""""""""

.. image:: uv_mappings/cylinder.svg


.. _file-type-3d:

3D Model
--------

3D models can be exported from almost any 3D modelling software, including
Blender and Maya.

As of right now, Tabletop Club supports the following 3D file formats:

* Collada (``.dae``)
* glTF 2.0 (``.glb``, ``.gltf``)
* Wavefront (``.obj``)

For convenience, the game will automatically set the centre-of-mass (COM) of the
object for you when it is imported. However, you can use the :ref:`config-cfg`
file to decide how the COM is adjusted.

* ``com_adjust = "off"``: The game will not adjust the COM. The COM will be at
  (0, 0, 0).

* ``com_adjust = "volume"`` *(default)*: The game will use the mid-point of the
  model's bounding box as the COM. The bounding box, or volume, is the smallest
  cube that contains all the model's vertices.

* ``com_adjust = "geometry"``: The game will use the average of all the model's
  vertices as the COM.

You can also specify how accurate the collision of the model is using the
``collision_mode`` property in the :ref:`config-cfg` file.

* ``collision_mode = 0`` *(default)*: The collision takes a *convex* shape,
  which is the simplest, but also the least accurate. If the model is hollow,
  other objects will not be able to go inside the model in this mode.

* ``collision_mode = 1``: The collision is made up of *multiple convex* shapes,
  which is slightly more accurate, but at the cost of performance (depending on
  the complexity of the model).

  If a model's collision is not acting in the way you expect, it is recommended
  to switch to this mode.

* ``collision_mode = 2``: The collision takes a *concave* shape, which is fully
  accurate, but also the heaviest on performance. Due to limitations with the
  game engine, concave models will not be able to collide with each other.

  This mode is recommended for models that are designed to be locked in place,
  like scenery or buildings.

.. note::

   When exporting 3D models with textures, make sure that the textures are also
   in the same folder as the exported model. You may also need to manually edit
   the file to check that the textures are not being loaded with an absolute
   file path, otherwise the textures won't work when the model is imported!


.. _file-type-audio:

Audio
-----

As of right now, Tabletop Club supports the following audio formats:

* MP3 (``.mp3``)
* Vorbis (``.ogg``)
* Waveform (``.wav``)

You can find out which format works best for you in the `importing audio page
<https://docs.godotengine.org/en/stable/getting_started/workflow/assets/importing_audio_samples.html>`_
in the Godot documentation.


.. _file-type-save:

Save File
---------

Save files are used to load back a saved state within Tabletop Club. They use
the ``.tc`` extension.

To create a save file when in-game, go to the menu and click
:guilabel:`Save game`, then choose a name to save the file as. You can then
load the state back by clicking the :guilabel:`Load game` button in the same
menu.

When saving, the game puts the save file under the
``<DOCUMENTS>/TabletopClub/saves`` folder, alongside a screenshot which is
taken when the save is made.

.. hint::

   If you don't want the screenshot to have the UI, you can toggle the UI
   before saving by pressing the :guilabel:`F9` key.
